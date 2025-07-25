# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
import socket
import sys
from typing import Dict, Any, Mapping, Union, cast
import msal

from azure.core.exceptions import ClientAuthenticationError
from azure.core.credentials import TokenRequestOptions
from azure.identity._credentials import (
    InteractiveBrowserCredential as _InteractiveBrowserCredential,
)  # pylint:disable=protected-access
from azure.identity._exceptions import CredentialUnavailableError  # pylint:disable=protected-access
from azure.identity._internal.utils import within_dac  # pylint:disable=protected-access
from ._utils import wrap_exceptions, resolve_tenant, is_wsl


class PopTokenRequestOptions(TokenRequestOptions):
    """Options to use for Proof-of-Possession (PoP) token requests."""

    pop: Union[bool, Mapping[str, str]]
    """PoP token request options.

    - If not specified or False, a non-PoP token request is made.
    - If True, an mTLS PoP token request is made.
    - If a dict, a Signed HTTP Request (SHR) PoP token request is made. The dict
      must contain the "resource_request_method", "resource_request_url", and "nonce" keys.
    """


class InteractiveBrowserBrokerCredential(_InteractiveBrowserCredential):
    """Uses an authentication broker to interactively sign in a user.

    Currently, only the following brokers are supported:
    - Web Account Manager (WAM) on Windows
    - Company Portal on macOS
    Users on Linux will be authenticated through the browser.

    :func:`~get_token` opens a browser to a login URL provided by Microsoft Entra ID and authenticates a user
    there with the authorization code flow, using PKCE (Proof Key for Code Exchange) internally to protect the code.

    :keyword str authority: Authority of a Microsoft Entra endpoint, for example "login.microsoftonline.com",
        the authority for Azure Public Cloud (which is the default). :class:`~azure.identity.AzureAuthorityHosts`
        defines authorities for other clouds.
    :keyword str tenant_id: a Microsoft Entra tenant ID. Defaults to the "organizations" tenant, which can
        authenticate work or school accounts.
    :keyword str client_id: Client ID of the Microsoft Entra application users will sign in to. If
        unspecified, users will authenticate to an Azure development application.
    :keyword str login_hint: a username suggestion to pre-fill the login page's username/email address field. A user
        may still log in with a different username.
    :keyword cache_persistence_options: configuration for persistent token caching. If unspecified, the credential
        will cache tokens in memory.
    :paramtype cache_persistence_options: ~azure.identity.TokenCachePersistenceOptions
    :keyword int timeout: seconds to wait for the user to complete authentication. Defaults to 300 (5 minutes).
    :keyword int parent_window_handle: If your app is a GUI app running on Windows 10+ or macOS, you
        are required to also provide its window handle, so that the sign in UI window will properly pop up on top
        of your window.
    :keyword bool use_default_broker_account: Enables automatically using the default broker account for
        authentication instead of prompting the user with an account picker. This is currently only supported on Windows
        and WSL. Defaults to False.
    :keyword bool enable_msa_passthrough: Determines whether Microsoft Account (MSA) passthrough is enabled. Note, this
        is only needed for select legacy first-party applications. Defaults to False.
    :keyword bool disable_instance_discovery: Determines whether or not instance discovery is performed when attempting
        to authenticate. Setting this to true will completely disable both instance discovery and authority validation.
        This functionality is intended for use in scenarios where the metadata endpoint cannot be reached, such as in
        private clouds or Azure Stack. The process of instance discovery entails retrieving authority metadata from
        https://login.microsoft.com/ to validate the authority. By setting this to **True**, the validation of the
        authority is disabled. As a result, it is crucial to ensure that the configured authority host is valid and
        trustworthy.
    :keyword bool enable_support_logging: Enables additional support logging in the underlying MSAL library.
        This logging potentially contains personally identifiable information and is intended to be used only for
        troubleshooting purposes.
    :raises ValueError: invalid **redirect_uri**
    """

    def __init__(self, **kwargs: Any) -> None:
        self._parent_window_handle = kwargs.pop("parent_window_handle", None)
        self._enable_msa_passthrough = kwargs.pop("enable_msa_passthrough", False)
        self._use_default_broker_account = kwargs.pop("use_default_broker_account", False)
        self._disable_interactive_fallback = kwargs.pop("disable_interactive_fallback", False)
        super().__init__(**kwargs)

    @wrap_exceptions
    def _request_token(self, *scopes: str, **kwargs: Any) -> Dict:
        scopes_list = list(scopes)
        claims = kwargs.get("claims")
        pop = kwargs.get("pop")
        app = cast(msal.PublicClientApplication, self._get_app(**kwargs))
        port = self._parsed_url.port if self._parsed_url else None
        auth_scheme = None
        if pop:
            auth_scheme = msal.PopAuthScheme(
                http_method=pop["resource_request_method"], url=pop["resource_request_url"], nonce=pop["nonce"]
            )
        if sys.platform.startswith("win") or is_wsl():
            result = {}
            if self._use_default_broker_account:
                try:
                    result = app.acquire_token_interactive(
                        scopes=scopes_list,
                        login_hint=self._login_hint,
                        claims_challenge=claims,
                        timeout=self._timeout,
                        prompt=msal.Prompt.NONE,
                        port=port,
                        parent_window_handle=self._parent_window_handle,
                        enable_msa_passthrough=self._enable_msa_passthrough,
                        auth_scheme=auth_scheme,
                    )
                    if "access_token" in result:
                        return result
                except socket.error:
                    pass

                if self._disable_interactive_fallback:
                    self._check_result(result)

            try:
                result = app.acquire_token_interactive(
                    scopes=scopes_list,
                    login_hint=self._login_hint,
                    claims_challenge=claims,
                    timeout=self._timeout,
                    prompt="select_account",
                    port=port,
                    parent_window_handle=self._parent_window_handle,
                    enable_msa_passthrough=self._enable_msa_passthrough,
                    auth_scheme=auth_scheme,
                )
            except socket.error as ex:
                raise CredentialUnavailableError(message="Couldn't start an HTTP server.") from ex

            self._check_result(result)
        else:
            try:
                result = app.acquire_token_interactive(
                    scopes=scopes_list,
                    login_hint=self._login_hint,
                    claims_challenge=claims,
                    timeout=self._timeout,
                    prompt="select_account",
                    port=port,
                    parent_window_handle=self._parent_window_handle,
                    enable_msa_passthrough=self._enable_msa_passthrough,
                    auth_scheme=auth_scheme,
                )
            except Exception:  # pylint: disable=broad-except
                app = cast(msal.PublicClientApplication, self._disable_broker_on_app(**kwargs))
                result = app.acquire_token_interactive(
                    scopes=scopes_list,
                    login_hint=self._login_hint,
                    claims_challenge=claims,
                    timeout=self._timeout,
                    prompt="select_account",
                    port=port,
                    parent_window_handle=self._parent_window_handle,
                    enable_msa_passthrough=self._enable_msa_passthrough,
                )
            self._check_result(result)
        return result

    def _check_result(self, result: Dict[str, Any]) -> None:
        if "access_token" not in result and "error_description" in result:
            if within_dac.get():
                raise CredentialUnavailableError(message=result["error_description"])
            raise ClientAuthenticationError(message=result.get("error_description"))
        if "access_token" not in result:
            if within_dac.get():
                raise CredentialUnavailableError(message="Failed to authenticate user")
            raise ClientAuthenticationError(message="Failed to authenticate user")

    def _get_app(self, **kwargs: Any) -> msal.ClientApplication:
        tenant_id = resolve_tenant(
            self._tenant_id, additionally_allowed_tenants=self._additionally_allowed_tenants, **kwargs
        )

        client_applications_map = self._client_applications
        capabilities = None
        token_cache = self._cache

        app_class = msal.PublicClientApplication

        if kwargs.get("enable_cae"):
            client_applications_map = self._cae_client_applications
            capabilities = ["CP1"]
            token_cache = self._cae_cache

        if not token_cache:
            token_cache = self._initialize_cache(is_cae=bool(kwargs.get("enable_cae")))

        if tenant_id not in client_applications_map:
            client_applications_map[tenant_id] = app_class(
                client_id=self._client_id,
                client_credential=self._client_credential,
                client_capabilities=capabilities,
                authority="{}/{}".format(self._authority, tenant_id),
                azure_region=self._regional_authority,
                token_cache=token_cache,
                http_client=self._client,
                instance_discovery=self._instance_discovery,
                enable_broker_on_windows=True,
                enable_broker_on_mac=True,
                enable_broker_on_linux=True,
                enable_broker_on_wsl=True,
                enable_pii_log=self._enable_support_logging,
            )

        return client_applications_map[tenant_id]

    def _disable_broker_on_app(self, **kwargs: Any) -> msal.ClientApplication:
        tenant_id = resolve_tenant(
            self._tenant_id, additionally_allowed_tenants=self._additionally_allowed_tenants, **kwargs
        )

        client_applications_map = self._client_applications
        capabilities = None
        token_cache = self._cache

        app_class = msal.PublicClientApplication

        if kwargs.get("enable_cae"):
            client_applications_map = self._cae_client_applications
            capabilities = ["CP1"]
            token_cache = self._cae_cache

        if not token_cache:
            token_cache = self._initialize_cache(is_cae=bool(kwargs.get("enable_cae")))

        client_applications_map[tenant_id] = app_class(
            client_id=self._client_id,
            client_credential=self._client_credential,
            client_capabilities=capabilities,
            authority="{}/{}".format(self._authority, tenant_id),
            azure_region=self._regional_authority,
            token_cache=token_cache,
            http_client=self._client,
            instance_discovery=self._instance_discovery,
            enable_broker_on_windows=False,
            enable_broker_on_mac=False,
            enable_broker_on_linux=False,
            enable_broker_on_wsl=False,
            enable_pii_log=self._enable_support_logging,
        )

        return client_applications_map[tenant_id]
