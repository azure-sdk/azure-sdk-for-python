# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import datetime
import json
import logging
import os
import random
import subprocess

from azure.monitor.opentelemetry.exporter._utils import PeriodicTask

logger = logging.getLogger(__name__)

ICACLS_PATH = os.path.join(
    os.environ.get("SYSTEMDRIVE", "C:"), r"\Windows\System32\icacls.exe"
)

def _fmt(timestamp):
    return timestamp.strftime("%Y-%m-%dT%H%M%S.%f")


def _now():
    return datetime.datetime.now(tz=datetime.timezone.utc)


def _seconds(seconds):
    return datetime.timedelta(seconds=seconds)


# pylint: disable=broad-except
class LocalFileBlob:
    def __init__(self, fullpath):
        self.fullpath = fullpath

    def delete(self):
        try:
            os.remove(self.fullpath)
        except Exception:
            pass  # keep silent

    def get(self):
        try:
            with open(self.fullpath, "r", encoding="utf-8") as file:
                return tuple(json.loads(line.strip()) for line in file.readlines())
        except Exception:
            pass  # keep silent
        return None

    def put(self, data, lease_period=0):
        try:
            fullpath = self.fullpath + ".tmp"
            with open(fullpath, "w", encoding="utf-8") as file:
                for item in data:
                    file.write(json.dumps(item))
                    # The official Python doc: Do not use os.linesep as a line
                    # terminator when writing files opened in text mode (the
                    # default); use a single '\n' instead, on all platforms.
                    file.write("\n")
            if lease_period:
                timestamp = _now() + _seconds(lease_period)
                self.fullpath += "@{}.lock".format(_fmt(timestamp))
            os.rename(fullpath, self.fullpath)
            return self
        except Exception:
            pass  # keep silent
        return None

    def lease(self, period):
        timestamp = _now() + _seconds(period)
        fullpath = self.fullpath
        if fullpath.endswith(".lock"):
            fullpath = fullpath[: fullpath.rindex("@")]
        fullpath += "@{}.lock".format(_fmt(timestamp))
        try:
            os.rename(self.fullpath, fullpath)
        except Exception:
            return None
        self.fullpath = fullpath
        return self


# pylint: disable=broad-except
class LocalFileStorage:
    def __init__(
        self,
        path,
        max_size=50 * 1024 * 1024,  # 50MiB
        maintenance_period=60,  # 1 minute
        retention_period=48 * 60 * 60,  # 48 hours
        write_timeout=60,  # 1 minute,
        name=None,
        lease_period=60,  # 1 minute
    ):
        self._path = os.path.abspath(path)
        self._max_size = max_size
        self._retention_period = retention_period
        self._write_timeout = write_timeout

        self._enabled = self._check_and_set_folder_permissions()
        if self._enabled:
            self._maintenance_routine()
            self._maintenance_task = PeriodicTask(
                interval=maintenance_period,
                function=self._maintenance_routine,
                name=name,
            )
            self._lease_period = lease_period
            self._maintenance_task.daemon = True
            self._maintenance_task.start()
        else:
            logger.error("Could not set secure permissions on storage folder, local storage is disabled.")

    def close(self):
        if self._enabled:
            self._maintenance_task.cancel()
            self._maintenance_task.join()

    def __enter__(self):
        return self

    # pylint: disable=redefined-builtin
    def __exit__(self, type, value, traceback):
        self.close()

    def _maintenance_routine(self):
        try:
            # pylint: disable=unused-variable
            for blob in self.gets():
                pass  # keep silent
        except Exception:
            pass  # keep silent

    # pylint: disable=too-many-nested-blocks
    def gets(self):
        if self._enabled:
            now = _now()
            lease_deadline = _fmt(now)
            retention_deadline = _fmt(now - _seconds(self._retention_period))
            timeout_deadline = _fmt(now - _seconds(self._write_timeout))
            try:
                for name in sorted(os.listdir(self._path)):
                    path = os.path.join(self._path, name)
                    if not os.path.isfile(path):
                        continue  # skip if not a file
                    if path.endswith(".tmp"):
                        if name < timeout_deadline:
                            try:
                                os.remove(path)  # TODO: log data loss
                            except Exception:
                                pass  # keep silent
                    if path.endswith(".lock"):
                        if path[path.rindex("@") + 1 : -5] > lease_deadline:
                            continue  # under lease
                        new_path = path[: path.rindex("@")]
                        try:
                            os.rename(path, new_path)
                        except Exception:
                            pass  # keep silent
                        path = new_path
                    if path.endswith(".blob"):
                        if name < retention_deadline:
                            try:
                                os.remove(path)  # TODO: log data loss
                            except Exception:
                                pass  # keep silent
                        else:
                            yield LocalFileBlob(path)
            except Exception:
                pass  # keep silent
        else:
            pass

    def get(self):
        if not self._enabled:
            return None
        cursor = self.gets()
        try:
            return next(cursor)
        except StopIteration:
            pass
        return None

    def put(self, data, lease_period=None):
        if not self._enabled:
            return None
        if not self._check_storage_size():
            return None
        blob = LocalFileBlob(
            os.path.join(
                self._path,
                "{}-{}.blob".format(
                    _fmt(_now()),
                    "{:08x}".format(random.getrandbits(32)),  # thread-safe random
                ),
            )
        )
        if lease_period is None:
            lease_period = self._lease_period
        return blob.put(data, lease_period=lease_period)

    def _check_and_set_folder_permissions(self):
        """
        Validate and set folder permissions where the telemetry data will be stored.
        :return: True if folder was created and permissions set successfully, False otherwise.
        :rtype: bool
        """
        try:
            # Create path if it doesn't exist
            os.makedirs(self._path, exist_ok=True)
            # Windows
            if os.name == "nt":
                user = self._get_current_user()
                if not user:
                    logger.warning(
                        "Failed to retrieve current user. Skipping folder permission setup."
                    )
                    return False
                result = subprocess.run(
                    [
                        ICACLS_PATH,
                        self._path,
                        "/grant",
                        "*S-1-5-32-544:(OI)(CI)F",  # Full permission for Administrators
                        f"{user}:(OI)(CI)F",
                        "/inheritance:r",
                    ],
                    check=False,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
                if result.returncode == 0:
                    return True
            # Unix
            else:
                os.chmod(self._path, 0o700)
                return True
        except Exception:
            pass  # keep silent
        return False

    def _check_storage_size(self):
        size = 0
        # pylint: disable=unused-variable
        for dirpath, dirnames, filenames in os.walk(self._path):
            for filename in filenames:
                path = os.path.join(dirpath, filename)
                # skip if it is symbolic link
                if not os.path.islink(path):
                    try:
                        size += os.path.getsize(path)
                    except OSError:
                        logger.error(
                            "Path %s does not exist or is inaccessible.",
                            path,
                        )
                        continue
                    if size >= self._max_size:
                        # pylint: disable=logging-format-interpolation
                        logger.warning(
                            "Persistent storage max capacity has been "
                            "reached. Currently at {}KB. Telemetry will be "
                            "lost. Please consider increasing the value of "
                            "'storage_max_size' in exporter config.".format(
                                str(size / 1024)
                            )
                        )
                        return False
        return True

    def _get_current_user(self):
        user = ""
        domain = os.environ.get("USERDOMAIN")
        username = os.environ.get("USERNAME")
        if domain and username:
            user = f"{domain}\\{username}"
        else:
            user = os.getlogin()
        return user
