# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
# pylint: disable=too-many-lines,too-many-public-methods
from datetime import datetime
from typing import Any, Dict, Optional, Union, List

from ._generated import models
from ._shared import parse_key_vault_id
from ._enums import (
    CertificatePolicyAction,
    KeyUsageType,
    KeyCurveName,
    KeyType,
    CertificateContentType,
    WellKnownIssuerNames,
)


class AdministratorContact(object):
    """Details of the organization administrator of the certificate issuer.

    :param first_name: First name of the issuer.
    :type first_name: str or None
    :param last_name: Last name of the issuer.
    :type last_name: str or None
    :param email: email of the issuer.
    :type email: str or None
    :param phone: phone number of the issuer.
    :type phone: str or None
    """

    def __init__(
        self,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        email: Optional[str] = None,
        phone: Optional[str] = None,
    ) -> None:
        self._first_name = first_name
        self._last_name = last_name
        self._phone = phone
        self._email = email

    def __repr__(self) -> str:
        result = (
            f"AdministratorContact(first_name={self.first_name}, last_name={self.last_name}, "
            + f"email={self.email}, phone={self.phone})"
        )
        return result[:1024]

    @classmethod
    def _from_admin_detail(cls, admin_detail: models.AdministratorDetails) -> "AdministratorContact":
        return cls(
            email=admin_detail.email_address,
            first_name=admin_detail.first_name,
            last_name=admin_detail.last_name,
            phone=admin_detail.phone,
        )

    @property
    def email(self) -> Optional[str]:
        """Email address of the issuer.

        :rtype: str or None"""
        return self._email

    @property
    def first_name(self) -> Optional[str]:
        """First name of the issuer.

        :rtype: str or None"""
        return self._first_name

    @property
    def last_name(self) -> Optional[str]:
        """Last name of the issuer.

        :rtype: str or None"""
        return self._last_name

    @property
    def phone(self) -> Optional[str]:
        """Phone number of the issuer.

        :rtype: str or None"""
        return self._phone


class CertificateOperationError(object):
    """The key vault server error.

    :param str code: The error code.
    :param str message: The error message.
    :param inner_error: The error object itself
    :type inner_error: ~azure.keyvault.certificates.CertificateOperationError or None
    """

    def __init__(self, code: str, message: str, inner_error: "Optional[CertificateOperationError]") -> None:
        self._code = code
        self._message = message
        self._inner_error = inner_error

    def __repr__(self) -> str:
        return f"CertificateOperationError({self.code}, {self.message}, {self.inner_error})"[:1024]

    @classmethod
    def _from_error_bundle(cls, error_bundle: models.KeyVaultErrorError) -> "CertificateOperationError":
        return cls(
            code=error_bundle.code,  # type: ignore
            message=error_bundle.message,  # type: ignore
            inner_error=cls._from_error_bundle(error_bundle.inner_error) if error_bundle.inner_error else None,
        )

    @property
    def code(self) -> str:
        """The error code.

        :returns: The error code.
        :rtype: str
        """
        return self._code

    @property
    def message(self) -> str:
        """The error message.

        :returns: The error message.
        :rtype: str
        """
        return self._message

    @property
    def inner_error(self) -> "Optional[CertificateOperationError]":
        """The error itself.

        :returns: The error itself.
        :rtype: ~azure.keyvault.certificates.CertificateOperationError or None
        """
        return self._inner_error


class CertificateProperties(object):
    """Certificate properties consists of a certificates metadata."""

    def __init__(self, **kwargs: Any) -> None:
        self._attributes = kwargs.pop("attributes", None)
        self._id = kwargs.pop("cert_id", None)
        self._vault_id = KeyVaultCertificateIdentifier(self._id)
        self._x509_thumbprint = kwargs.pop("x509_thumbprint", None)
        self._tags = kwargs.pop("tags", None)
        self._preserve_order = kwargs.pop("preserve_order", False)

    def __repr__(self) -> str:
        return f"<CertificateProperties [{self._x509_thumbprint.hex().upper()}]>"[:1024]

    @classmethod
    def _from_certificate_bundle(
        cls,
        certificate_bundle: Union[
            models.CertificateBundle,
            models.DeletedCertificateBundle,
        ],
    ) -> "CertificateProperties":
        return cls(
            attributes=certificate_bundle.attributes,
            cert_id=certificate_bundle.id,
            x509_thumbprint=certificate_bundle.x509_thumbprint,
            tags=certificate_bundle.tags,
            preserve_order=certificate_bundle.preserve_cert_order,
        )

    @classmethod
    def _from_certificate_item(
        cls,
        certificate_item: Union[
            models.CertificateItem,
            models.DeletedCertificateItem,
        ],
    ) -> "CertificateProperties":
        return cls(
            attributes=certificate_item.attributes,
            cert_id=certificate_item.id,
            x509_thumbprint=certificate_item.x509_thumbprint,
            tags=certificate_item.tags,
        )

    @property
    def id(self) -> str:
        """The certificate identifier.

        :returns: The certificate identifier.
        :rtype: str
        """
        return self._id

    @property
    def name(self) -> str:
        """The name of the certificate.

        :returns: The name of the certificate.
        :rtype: str
        """
        return self._vault_id.name

    @property
    def enabled(self) -> Optional[bool]:
        """Whether the certificate is enabled or not.

        :returns: True if the certificate is enabled; False otherwise.
        :rtype: bool or None
        """
        return self._attributes.enabled if self._attributes else None

    @property
    def not_before(self) -> Optional[datetime]:
        """The datetime before which the certificate is not valid.

        :returns: A datetime representing the point in time when the certificate becomes valid.
        :rtype: ~datetime.datetime or None
        """
        return self._attributes.not_before if self._attributes else None

    @property
    def expires_on(self) -> Optional[datetime]:
        """The datetime when the certificate expires.

        :returns: A datetime representing the point in time when the certificate expires.
        :rtype: ~datetime.datetime or None
        """
        return self._attributes.expires if self._attributes else None

    @property
    def created_on(self) -> Optional[datetime]:
        """The datetime when the certificate is created.

        :returns: A datetime representing the certificate's creation time.
        :rtype: ~datetime.datetime or None
        """
        return self._attributes.created if self._attributes else None

    @property
    def updated_on(self) -> Optional[datetime]:
        """The datetime when the certificate was last updated.

        :returns: A datetime representing the time of the certificate's most recent update.
        :rtype: ~datetime.datetime or None
        """
        return self._attributes.updated if self._attributes else None

    @property
    def recoverable_days(self) -> Optional[int]:
        """The number of days the certificate is retained before being deleted from a soft-delete enabled Key Vault.

        :returns: The number of days remaining where the certificate can be restored.
        :rtype: int or None
        """
        # recoverable_days was added in 7.1-preview
        if self._attributes and hasattr(self._attributes, "recoverable_days"):
            return self._attributes.recoverable_days
        return None

    @property
    def recovery_level(self) -> Optional[models.DeletionRecoveryLevel]:
        """The deletion recovery level currently in effect for the certificate.

        :returns: The deletion recovery level currently in effect for the certificate.
        :rtype: models.DeletionRecoveryLevel or None
        """
        return self._attributes.recovery_level if self._attributes else None

    @property
    def vault_url(self) -> str:
        """The URL of the vault containing the certificate.

        :returns: The URL of the vault containing the certificate.
        :rtype: str
        """
        return self._vault_id.vault_url

    @property
    def x509_thumbprint(self) -> bytes:
        """The certificate's thumbprint, in bytes.

        To get the thumbprint as a hexadecimal string, call ``.hex()`` on this property.

        :return: The certificate's thumbprint, in bytes.
        :rtype: bytes
        """
        return self._x509_thumbprint

    @property
    def tags(self) -> Optional[Dict[str, str]]:
        """Application specific metadata in the form of key-value pairs.

        :returns: A dictionary of tags attached to the certificate.
        :rtype: dict[str, str] or None
        """
        return self._tags

    @property
    def version(self) -> Optional[str]:
        """The version of the certificate.

        :returns: The version of the certificate.
        :rtype: str or None
        """
        return self._vault_id.version

    @property
    def preserve_order(self) -> Optional[bool]:
        """Whether the certificate order should be preserved.

        :returns: Specifies whether the certificate chain preserves its original order. The default value is False, 
            which sets the leaf certificate at index 0.
        :rtype: bool or None
        """
        return self._preserve_order


class KeyVaultCertificate(object):
    """Consists of a certificate and its attributes

    :param policy: The management policy for the certificate.
    :type policy: ~azure.keyvault.certificates.CertificatePolicy or None
    :param properties: The certificate's properties.
    :type properties: ~azure.keyvault.certificates.CertificateProperties or None
    :param cer: CER contents of the X509 certificate.
    :type cer: bytearray or None
    """

    def __init__(
        self,
        policy: "Optional[CertificatePolicy]" = None,
        properties: Optional[CertificateProperties] = None,
        cer: Optional[bytearray] = None,
        **kwargs: Any,
    ) -> None:
        self._properties = properties
        self._key_id = kwargs.get("key_id", None)
        self._secret_id = kwargs.get("secret_id", None)
        self._policy = policy
        self._cer = cer

    def __repr__(self) -> str:
        return f"<KeyVaultCertificate [{self.id}]>"[:1024]

    @classmethod
    def _from_certificate_bundle(cls, certificate_bundle: models.CertificateBundle) -> "KeyVaultCertificate":
        # pylint:disable=protected-access

        if certificate_bundle.policy:
            policy: Optional[CertificatePolicy] = CertificatePolicy._from_certificate_policy_bundle(
                certificate_bundle.policy
            )
        else:
            policy = None

        return cls(
            properties=CertificateProperties._from_certificate_bundle(certificate_bundle),
            key_id=certificate_bundle.kid,
            secret_id=certificate_bundle.sid,
            policy=policy,
            cer=certificate_bundle.cer,  # type: ignore
        )

    @property
    def id(self) -> Optional[str]:
        """The certificate identifier.

        :returns: The certificate identifier.
        :rtype: str or None
        """
        return self._properties.id if self._properties else None

    @property
    def name(self) -> Optional[str]:
        """The name of the certificate.

        :returns: The name of the certificate.
        :rtype: str or None
        """
        return self._properties.name if self._properties else None

    @property
    def properties(self) -> Optional[CertificateProperties]:
        """The certificate's properties.

        :returns: The certificate's properties.
        :rtype: ~azure.keyvault.certificates.CertificateProperties or None
        """
        return self._properties

    @property
    def key_id(self) -> Optional[str]:
        """The ID of the key associated with the certificate.

        :returns: The ID of the key associated with the certificate.
        :rtype: str or None
        """
        return self._key_id

    @property
    def secret_id(self) -> Optional[str]:
        """The ID of the secret associated with the certificate.

        :returns: The ID of the secret associated with the certificate.
        :rtype: str or None
        """
        return self._secret_id

    @property
    def policy(self) -> "Optional[CertificatePolicy]":
        """The management policy of the certificate.

        :returns: The management policy of the certificate.
        :rtype: ~azure.keyvault.certificates.CertificatePolicy or None
        """
        return self._policy

    @property
    def cer(self) -> Optional[bytearray]:
        """The CER contents of the certificate.

        :returns: The CER contents of the certificate.
        :rtype: bytearray or None
        """
        return self._cer


class KeyVaultCertificateIdentifier(object):
    """Information about a KeyVaultCertificate parsed from a certificate ID.

    :param str source_id: the full original identifier of a certificate

    :raises ValueError: if the certificate ID is improperly formatted

    Example:
        .. literalinclude:: ../tests/test_parse_id.py
            :start-after: [START parse_key_vault_certificate_id]
            :end-before: [END parse_key_vault_certificate_id]
            :language: python
            :caption: Parse a certificate's ID
            :dedent: 8
    """

    def __init__(self, source_id: str) -> None:
        self._resource_id = parse_key_vault_id(source_id)

    @property
    def source_id(self) -> str:
        return self._resource_id.source_id

    @property
    def vault_url(self) -> str:
        return self._resource_id.vault_url

    @property
    def name(self) -> str:
        return self._resource_id.name

    @property
    def version(self) -> Optional[str]:
        return self._resource_id.version


class CertificateOperation(object):
    # pylint:disable=too-many-instance-attributes
    """A certificate operation is returned in case of long running requests.

    :param cert_operation_id: The certificate id.
    :type cert_operation_id: str or None
    :param issuer_name: Name of the operation's issuer object or reserved names.
    :type issuer_name: str or ~azure.keyvault.certificates.WellKnownIssuerNames or None
    :param certificate_type: Type of certificate requested from the issuer provider.
    :type certificate_type: str or None
    :param certificate_transparency: Indicates if the certificate this operation is running for is published to
        certificate transparency logs. Defaults to False.
    :type certificate_transparency: bool or None
    :param csr: The certificate signing request (CSR) that is being used in the certificate operation.
    :type csr: bytes or None
    :param cancellation_requested: Indicates if cancellation was requested on the certificate operation. Defaults
        to False.
    :type cancellation_requested: bool or None
    :param status: Status of the certificate operation.
    :type status: str or None
    :param status_details: The status details of the certificate operation
    :type status_details: str or None
    :param error: Error encountered, if any, during the certificate operation.
    :type error: ~azure.keyvault.certificates.CertificateOperationError or None
    :param target: Location which contains the result of the certificate operation.
    :type target: str or None
    :param request_id: Identifier for the certificate operation.
    :type request_id: str or None
    :param bool preserve_order: Specifies whether the certificate chain preserves its original order. The default
        value is False, which sets the leaf certificate at index 0.
    """

    def __init__(
        self,
        cert_operation_id: Optional[str] = None,
        issuer_name: Optional[Union[str, WellKnownIssuerNames]] = None,
        certificate_type: Optional[str] = None,
        certificate_transparency: Optional[bool] = False,
        csr: Optional[bytes] = None,
        cancellation_requested: Optional[bool] = False,
        status: Optional[str] = None,
        status_details: Optional[str] = None,
        error: Optional[CertificateOperationError] = None,
        target: Optional[str] = None,
        request_id: Optional[str] = None,
        preserve_order: Optional[bool] = False,
    ) -> None:
        self._id = cert_operation_id
        self._vault_id = parse_key_vault_id(cert_operation_id) if cert_operation_id else None
        self._issuer_name = issuer_name
        self._certificate_type = certificate_type
        self._certificate_transparency = certificate_transparency
        self._csr = csr
        self._cancellation_requested = cancellation_requested
        self._status = status
        self._status_details = status_details
        self._error = error
        self._target = target
        self._request_id = request_id
        self._preserve_order = preserve_order

    def __repr__(self) -> str:
        return f"<CertificateOperation [{self.id}]>"[:1024]

    @classmethod
    def _from_certificate_operation_bundle(
        cls, certificate_operation_bundle: models.CertificateOperation
    ) -> "CertificateOperation":

        issuer_parameters = certificate_operation_bundle.issuer_parameters
        return cls(
            cert_operation_id=certificate_operation_bundle.id,
            issuer_name=issuer_parameters.name if issuer_parameters else None,
            certificate_type=(
                certificate_operation_bundle.issuer_parameters.certificate_type
                if certificate_operation_bundle.issuer_parameters
                else None
            ),
            # 2016-10-01 IssuerParameters doesn't have certificate_transparency
            certificate_transparency=getattr(issuer_parameters, "certificate_transparency", None),
            csr=certificate_operation_bundle.csr,
            cancellation_requested=certificate_operation_bundle.cancellation_requested,
            status=certificate_operation_bundle.status,
            status_details=certificate_operation_bundle.status_details,
            error=(
                CertificateOperationError._from_error_bundle(  # pylint: disable=protected-access
                    certificate_operation_bundle.error
                )
                if certificate_operation_bundle.error
                else None
            ),
            target=certificate_operation_bundle.target,
            request_id=certificate_operation_bundle.request_id,
            preserve_order=certificate_operation_bundle.preserve_cert_order,
        )

    @property
    def id(self) -> Optional[str]:
        """The certificate ID.

        :returns: The certificate ID.
        :rtype: str or None
        """
        return self._id

    @property
    def name(self) -> Optional[str]:
        """The certificate name.

        :returns: The certificate name.
        :rtype: str or None
        """
        return self._vault_id.name if self._vault_id else None

    @property
    def vault_url(self) -> Optional[str]:
        """URL of the vault performing the certificate operation.

        :returns: URL of the vault performing the certificate operation.
        :rtype: str or None
        """
        return self._vault_id.vault_url if self._vault_id else None

    @property
    def issuer_name(self) -> Union[str, WellKnownIssuerNames, None]:
        """The name of the certificate issuer.

        :returns: The name of the certificate issuer.
        :rtype: str or ~azure.keyvault.certificates.WellKnownIssuerNames or None
        """
        return self._issuer_name

    @property
    def certificate_type(self) -> Optional[str]:
        """Type of certificate to be requested from the issuer provider.

        :returns: Type of certificate to be requested from the issuer provider.
        :rtype: str or None
        """
        return self._certificate_type

    @property
    def certificate_transparency(self) -> Optional[bool]:
        """Whether certificates generated under this policy should be published to certificate transparency logs.

        :returns: True if the certificates should be published to transparency logs; False otherwise.
        :rtype: bool or None
        """
        return self._certificate_transparency

    @property
    def csr(self) -> Optional[bytes]:
        """The certificate signing request that is being used in this certificate operation.

        :returns: The certificate signing request that is being used in this certificate operation.
        :rtype: bytes or None
        """
        return self._csr

    @property
    def cancellation_requested(self) -> Optional[bool]:
        """Whether cancellation was requested on the certificate operation.

        :returns: True if cancellation was requested; False otherwise.
        :rtype: bool or None
        """
        return self._cancellation_requested

    @property
    def status(self) -> Optional[str]:
        """The operation status.

        :returns: The operation status.
        :rtype: str or None
        """
        return self._status

    @property
    def status_details(self) -> Optional[str]:
        """Details of the operation status.

        :returns: Details of the operation status.
        :rtype: str or None
        """
        return self._status_details

    @property
    def error(self) -> Optional[CertificateOperationError]:
        """Any error associated with the certificate operation.

        :returns: Any error associated with the operation, as a
            :class:`~azure.keyvault.certificates.CertificateOperationError`.
        :rtype: ~azure.keyvault.certificates.CertificateOperationError or None"""
        return self._error

    @property
    def target(self) -> Optional[str]:
        """Location which contains the result of the certificate operation.

        :returns: Location which contains the result of the certificate operation.
        :rtype: str or None
        """
        return self._target

    @property
    def request_id(self) -> Optional[str]:
        """Identifier for the certificate operation.

        :returns: Identifier for the certificate operation.
        :rtype: str or None
        """
        return self._request_id

    @property
    def preserve_order(self) -> Optional[bool]:
        """Whether the certificate order should be preserved.

        :returns: Specifies whether the certificate chain preserves its original order. The default value is False,
            which sets the leaf certificate at index 0.
        :rtype: bool or None
        """
        return self._preserve_order


class CertificatePolicy(object):
    """Management policy for a certificate.

    :param issuer_name: Optional. Name of the referenced issuer object or reserved names; for example,
        :attr:`~azure.keyvault.certificates.WellKnownIssuerNames.self` or
        :attr:`~azure.keyvault.certificates.WellKnownIssuerNames.unknown`
    :type issuer_name: str or None

    :keyword subject: The subject name of the certificate. Should be a valid X509 distinguished name. Either subject or
        one of the subject alternative name parameters are required for creating a certificate. This will be ignored
        when importing a certificate; the subject will be parsed from the imported certificate.
    :paramtype subject: str or None
    :keyword san_emails: Subject alternative emails of the X509 object. Either subject or one of the subject alternative
        name parameters are required for creating a certificate.
    :paramtype san_emails: list[str] or None
    :keyword san_dns_names: Subject alternative DNS names of the X509 object. Either subject or one of the subject
        alternative name parameters are required for creating a certificate.
    :paramtype san_dns_names: list[str] or None
    :keyword san_user_principal_names: Subject alternative user principal names of the X509 object. Either subject or
        one of the subject alternative name parameters are required for creating a certificate.
    :paramtype san_user_principal_names: list[str] or None
    :keyword exportable: Indicates if the private key can be exported. For valid values, see KeyType.
    :paramtype exportable: bool or None
    :keyword key_type: The type of key pair to be used for the certificate.
    :paramtype key_type: str or ~azure.keyvault.certificates.KeyType or None
    :keyword key_size: The key size in bits. For example: 2048, 3072, or 4096 for RSA.
    :paramtype key_size: int or None
    :keyword reuse_key: Indicates if the same key pair will be used on certificate renewal.
    :paramtype reuse_key: bool or None
    :keyword key_curve_name: Elliptic curve name. For valid values, see KeyCurveName.
    :paramtype key_curve_name: str or ~azure.keyvault.certificates.KeyCurveName or None
    :keyword enhanced_key_usage: The extended ways the key of the certificate can be used.
    :paramtype enhanced_key_usage: list[str] or None
    :keyword key_usage: List of key usages.
    :paramtype key_usage: list[str or ~azure.keyvault.certificates.KeyUsageType] or None
    :keyword content_type: The media type (MIME type) of the secret backing the certificate.  If not specified,
        :attr:`CertificateContentType.pkcs12` is assumed.
    :paramtype content_type: str or ~azure.keyvault.certificates.CertificateContentType or None
    :keyword validity_in_months: The duration that the certificate is valid in months.
    :paramtype validity_in_months: int or None
    :keyword lifetime_actions: Actions that will be performed by Key Vault over the lifetime of a certificate.
    :paramtype lifetime_actions: list[~azure.keyvault.certificates.LifetimeAction] or None
    :keyword certificate_type: Type of certificate to be requested from the issuer provider.
    :paramtype certificate_type: str or None
    :keyword certificate_transparency: Indicates if the certificates generated under this policy should be
        published to certificate transparency logs.
    :paramtype certificate_transparency: bool or None
    """

    # pylint:disable=too-many-instance-attributes
    def __init__(
        self,
        issuer_name: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        self._issuer_name = issuer_name
        self._subject = kwargs.pop("subject", None)
        self._attributes = kwargs.pop("attributes", None)
        self._exportable = kwargs.pop("exportable", None)
        self._key_type = kwargs.pop("key_type", None)
        self._key_size = kwargs.pop("key_size", None)
        self._reuse_key = kwargs.pop("reuse_key", None)
        self._key_curve_name = kwargs.pop("key_curve_name", None)
        self._enhanced_key_usage = kwargs.pop("enhanced_key_usage", None)
        self._key_usage = kwargs.pop("key_usage", None)
        self._content_type = kwargs.pop("content_type", None)
        self._validity_in_months = kwargs.pop("validity_in_months", None)
        self._lifetime_actions = kwargs.pop("lifetime_actions", None)
        self._certificate_type = kwargs.pop("certificate_type", None)
        self._certificate_transparency = kwargs.pop("certificate_transparency", None)
        self._san_emails = kwargs.pop("san_emails", None) or None
        self._san_dns_names = kwargs.pop("san_dns_names", None) or None
        self._san_user_principal_names = kwargs.pop("san_user_principal_names", None) or None

    @classmethod
    def get_default(cls) -> "CertificatePolicy":
        return cls(issuer_name=WellKnownIssuerNames.self, subject="CN=DefaultPolicy")

    def __repr__(self) -> str:
        return f"<CertificatePolicy [issuer_name: {self.issuer_name}]>"[:1024]

    def _to_certificate_policy_bundle(self) -> models.CertificatePolicy:
        if self.issuer_name or self.certificate_type or self.certificate_transparency:
            issuer_parameters: Optional[models.IssuerParameters] = models.IssuerParameters(
                name=self.issuer_name,
                certificate_type=self.certificate_type,
                certificate_transparency=self.certificate_transparency,  # 2016-10-01 model will ignore this
            )
        else:
            issuer_parameters = None

        if self.enabled is not None or self.created_on is not None or self.updated_on is not None:
            attributes = models.CertificateAttributes(
                {
                    "enabled": self.enabled,
                    "created": self.created_on,
                    "updated": self.updated_on,
                }
            )
        else:
            attributes = None

        if self.lifetime_actions:
            lifetime_actions = []
            for lifetime_action in self.lifetime_actions:
                lifetime_actions.append(
                    models.LifetimeAction(
                        trigger=models.Trigger(
                            lifetime_percentage=lifetime_action.lifetime_percentage,
                            days_before_expiry=lifetime_action.days_before_expiry,
                        ),
                        action=models.Action(action_type=lifetime_action.action),
                    )
                )
        else:
            lifetime_actions = None  # type: ignore

        # pylint:disable=too-many-boolean-expressions
        if (
            self.subject
            or self.enhanced_key_usage
            or self.key_usage
            or self.san_emails
            or self.san_user_principal_names
            or self.san_dns_names
            or self.validity_in_months
        ):
            if self.key_usage:
                key_usage: Optional[List[Union[str, KeyUsageType]]] = [
                    k.value if not isinstance(k, str) else k for k in self.key_usage
                ]
            else:
                key_usage = None

            x509_properties: Optional[models.X509CertificateProperties] = models.X509CertificateProperties(
                subject=self.subject,
                ekus=self.enhanced_key_usage,
                subject_alternative_names=models.SubjectAlternativeNames(
                    emails=self.san_emails, upns=self.san_user_principal_names, dns_names=self.san_dns_names
                ),
                key_usage=key_usage,
                validity_in_months=self.validity_in_months,
            )
        else:
            x509_properties = None

        if self.exportable or self.key_type or self.key_size or self.reuse_key or self.key_curve_name:
            key_properties: Optional[models.KeyProperties] = models.KeyProperties(
                exportable=self.exportable,
                key_type=self.key_type,
                key_size=self.key_size,
                reuse_key=self.reuse_key,
                curve=self.key_curve_name,
            )
        else:
            key_properties = None

        if self.content_type:
            secret_properties: Optional[models.SecretProperties] = models.SecretProperties(
                content_type=self.content_type
            )
        else:
            secret_properties = None

        policy_bundle = models.CertificatePolicy(
            key_properties=key_properties,
            secret_properties=secret_properties,
            x509_certificate_properties=x509_properties,
            lifetime_actions=lifetime_actions,
            issuer_parameters=issuer_parameters,
            attributes=attributes,
        )
        return policy_bundle

    @classmethod
    def _from_certificate_policy_bundle(
        cls, certificate_policy_bundle: Optional[models.CertificatePolicy]
    ) -> "CertificatePolicy":
        if certificate_policy_bundle is None:
            return cls()

        if certificate_policy_bundle.lifetime_actions:
            lifetime_actions: Optional[List[LifetimeAction]] = [
                LifetimeAction(
                    action=CertificatePolicyAction(item.action.action_type) if item.action else None,
                    lifetime_percentage=item.trigger.lifetime_percentage if item.trigger else None,
                    days_before_expiry=item.trigger.days_before_expiry if item.trigger else None,
                )
                for item in certificate_policy_bundle.lifetime_actions
            ]
        else:
            lifetime_actions = None
        x509_certificate_properties = certificate_policy_bundle.x509_certificate_properties
        if x509_certificate_properties and x509_certificate_properties.key_usage:
            key_usage: Optional[List[KeyUsageType]] = [KeyUsageType(k) for k in x509_certificate_properties.key_usage]
        else:
            key_usage = None
        key_properties = certificate_policy_bundle.key_properties
        curve_name = getattr(key_properties, "curve", None)  # missing from 2016-10-01 KeyProperties
        if curve_name:
            curve_name = KeyCurveName(curve_name)

        issuer_parameters = certificate_policy_bundle.issuer_parameters
        return cls(
            issuer_name=issuer_parameters.name if issuer_parameters else None,
            subject=(x509_certificate_properties.subject if x509_certificate_properties else None),
            certificate_type=issuer_parameters.certificate_type if issuer_parameters else None,
            # 2016-10-01 IssuerParameters doesn't have certificate_transparency
            certificate_transparency=getattr(issuer_parameters, "certificate_transparency", None),
            lifetime_actions=lifetime_actions,
            exportable=key_properties.exportable if key_properties else None,
            key_type=KeyType(key_properties.key_type) if key_properties and key_properties.key_type else None,
            key_size=key_properties.key_size if key_properties else None,
            reuse_key=key_properties.reuse_key if key_properties else None,
            key_curve_name=curve_name,
            enhanced_key_usage=x509_certificate_properties.ekus if x509_certificate_properties else None,
            key_usage=key_usage,
            content_type=(
                CertificateContentType(certificate_policy_bundle.secret_properties.content_type)
                if certificate_policy_bundle.secret_properties
                and certificate_policy_bundle.secret_properties.content_type
                else None
            ),
            attributes=certificate_policy_bundle.attributes,
            san_emails=(
                x509_certificate_properties.subject_alternative_names.emails
                if x509_certificate_properties and x509_certificate_properties.subject_alternative_names
                else None
            ),
            san_user_principal_names=(
                x509_certificate_properties.subject_alternative_names.upns
                if x509_certificate_properties and x509_certificate_properties.subject_alternative_names
                else None
            ),
            san_dns_names=(
                x509_certificate_properties.subject_alternative_names.dns_names
                if x509_certificate_properties and x509_certificate_properties.subject_alternative_names
                else None
            ),
            validity_in_months=(
                x509_certificate_properties.validity_in_months if x509_certificate_properties else None
            ),
        )

    @property
    def exportable(self) -> Optional[bool]:
        """Whether the private key can be exported.

        :returns: True if the private key can be exported; False otherwise.
        :rtype: bool or None
        """
        return self._exportable

    @property
    def key_type(self) -> Optional[KeyType]:
        """The type of key pair to be used for the certificate.

        :returns: The type of key pair to be used for the certificate.
        :rtype: ~azure.keyvault.certificates.KeyType or None
        """
        return self._key_type

    @property
    def key_size(self) -> Optional[int]:
        """The key size in bits.

        :returns: The key size in bits.
        :rtype: int or None
        """
        return self._key_size

    @property
    def reuse_key(self) -> Optional[bool]:
        """Whether the same key pair will be used on certificate renewal.

        :returns: True if the same key pair will be used on certificate renewal; False otherwise.
        :rtype: bool or None
        """
        return self._reuse_key

    @property
    def key_curve_name(self) -> Optional[KeyCurveName]:
        """Elliptic curve name.

        :returns: Elliptic curve name.
        :rtype: ~azure.keyvault.certificates.KeyCurveName or None
        """
        return self._key_curve_name

    @property
    def enhanced_key_usage(self) -> Optional[List[str]]:
        """The enhanced key usage.

        :returns: The enhanced key usage.
        :rtype: list[str] or None
        """
        return self._enhanced_key_usage

    @property
    def key_usage(self) -> Optional[List[KeyUsageType]]:
        """List of key usages.

        :returns: List of key usages.
        :rtype: list[~azure.keyvault.certificates.KeyUsageType] or None
        """
        return self._key_usage

    @property
    def content_type(self) -> Optional[CertificateContentType]:
        """The media type (MIME type).

        :returns: The media type (MIME type).
        :rtype: ~azure.keyvault.certificates.CertificateContentType or None
        """
        return self._content_type

    @property
    def subject(self) -> Optional[str]:
        """The subject name of the certificate.

        :returns: The subject name of the certificate.
        :rtype: str or None
        """
        return self._subject

    @property
    def san_emails(self) -> Optional[List[str]]:
        """The subject alternative email addresses.

        :returns: The subject alternative email addresses, as a list.
        :rtype: list[str] or None
        """
        return self._san_emails

    @property
    def san_dns_names(self) -> Optional[List[str]]:
        """The subject alternative domain names.

        :returns: The subject alternative domain names, as a list.
        :rtype: list[str] or None
        """
        return self._san_dns_names

    @property
    def san_user_principal_names(self) -> Optional[List[str]]:
        """The subject alternative user principal names.

        :returns: The subject alternative user principal names, as a list.
        :rtype: list[str] or None
        """
        return self._san_user_principal_names

    @property
    def validity_in_months(self) -> Optional[int]:
        """The duration that the certificate is valid for in months.

        :returns: The duration that the certificate is valid for in months.
        :rtype: int or None
        """
        return self._validity_in_months

    @property
    def lifetime_actions(self) -> "Optional[List[LifetimeAction]]":
        """Actions and their triggers that will be performed by Key Vault over the lifetime of the certificate.

        :returns: Actions and their triggers that will be performed by Key Vault over the lifetime of the certificate.
        :rtype: list[~azure.keyvault.certificates.LifetimeAction] or None
        """
        return self._lifetime_actions

    @property
    def issuer_name(self) -> Optional[str]:
        """Name of the referenced issuer object or reserved names for the issuer of the certificate.

        :returns: Name of the referenced issuer object or reserved names for the issuer of the certificate.
        :rtype: str or None
        """
        return self._issuer_name

    @property
    def certificate_type(self) -> Optional[str]:
        """Type of certificate requested from the issuer provider.

        :returns: Type of certificate requested from the issuer provider.
        :rtype: str or None
        """
        return self._certificate_type

    @property
    def certificate_transparency(self) -> Optional[bool]:
        """Whether the certificates generated under this policy should be published to certificate transparency logs.

        :returns: True if the certificates should be published to transparency logs; False otherwise.
        :rtype: bool or None
        """
        return self._certificate_transparency

    @property
    def enabled(self) -> Optional[bool]:
        """Whether the certificate is enabled or not.

        :returns: True if the certificate is enabled; False otherwise.
        :rtype: bool or None
        """
        return self._attributes.enabled if self._attributes else None

    @property
    def created_on(self) -> Optional[datetime]:
        """The datetime when the certificate is created.

        :returns: The datetime when the certificate is created.
        :rtype: ~datetime.datetime or None
        """
        return self._attributes.created if self._attributes else None

    @property
    def updated_on(self) -> Optional[datetime]:
        """The datetime when the certificate was last updated.

        :returns: The datetime when the certificate was last updated.
        :rtype: ~datetime.datetime or None
        """
        return self._attributes.updated if self._attributes else None


class CertificateContact(object):
    """The contact information for the vault certificates.

    :param email: Email address of a contact for the certificate.
    :type email: str or None
    :param name: Name of a contact for the certificate.
    :type name: str or None
    :param phone: phone number of a contact for the certificate.
    :type phone: str or None
    """

    def __init__(self, email: Optional[str] = None, name: Optional[str] = None, phone: Optional[str] = None) -> None:
        self._email = email
        self._name = name
        self._phone = phone

    def __repr__(self) -> str:
        return f"CertificateContact(email={self.email}, name={self.name}, phone={self.phone})"[:1024]

    def _to_certificate_contacts_item(self) -> models.Contact:
        return models.Contact(email_address=self.email, name=self.name, phone=self.phone)

    @classmethod
    def _from_certificate_contacts_item(cls, contact_item: models.Contact) -> "CertificateContact":
        return cls(email=contact_item.email_address, name=contact_item.name, phone=contact_item.phone)

    @property
    def email(self) -> Optional[str]:
        """Email address of a contact for the certificate.

        :rtype: str or None"""
        return self._email

    @property
    def name(self) -> Optional[str]:
        """Name of a contact for the certificate.

        :rtype: str or None"""
        return self._name

    @property
    def phone(self) -> Optional[str]:
        """Phone number of a contact for the certificate.

        :rtype: str or None"""
        return self._phone


class IssuerProperties(object):
    """The properties of an issuer containing the issuer metadata.

    :param provider: The issuer provider.
    :type provider: str or None
    """

    def __init__(self, provider: Optional[str] = None, **kwargs: Any) -> None:
        self._id = kwargs.pop("issuer_id", None)
        self._vault_id = parse_key_vault_id(self._id)
        self._provider = provider

    def __repr__(self) -> str:
        return f"IssuerProperties(issuer_id={self.id}, provider={self.provider})"[:1024]

    @classmethod
    def _from_issuer_item(
        cls, issuer_item: Union[models.CertificateIssuerItem, models.IssuerBundle]
    ) -> "IssuerProperties":
        return cls(issuer_id=issuer_item.id, provider=issuer_item.provider)

    @property
    def id(self) -> Optional[str]:
        """The issuer ID.

        :returns: The issuer ID.
        :rtype: str or None
        """
        return self._id

    @property
    def name(self) -> Optional[str]:
        """The issuer name.

        :returns: The issuer name.
        :rtype: str or None
        """
        # Issuer name is listed under version under vault_id
        return self._vault_id.version

    @property
    def provider(self) -> Optional[str]:
        """The issuer provider.

        :returns: The issuer provider.
        :rtype: str or None
        """
        return self._provider


class CertificateIssuer(object):
    """The issuer for a Key Vault certificate.

    :param provider: The issuer provider
    :type provider: str or None
    :param attributes: The issuer attributes.
    :type attributes: ~azure.keyvault.certificates._generated.models.IssuerAttributes or None
    :param account_id: The username / account name / account id.
    :type account_id: str or None
    :param password: The password / secret / account key.
    :type password: str or None
    :param organization_id: The ID of the organization.
    :type organization_id: str or None
    :param admin_contacts: Details of the organization administrator.
    :type admin_contacts: list[~azure.keyvault.certificates.AdministratorContact] or None
    """

    def __init__(
        self,
        provider: Optional[str],
        attributes: Optional[models.IssuerAttributes] = None,
        account_id: Optional[str] = None,
        # [SuppressMessage("Microsoft.Security", "CS002:SecretInNextLine", Justification="Typedef, not string.")]
        password: Optional[str] = None,
        organization_id: Optional[str] = None,
        admin_contacts: Optional[List[AdministratorContact]] = None,
        **kwargs: Any,
    ) -> None:
        self._provider = provider
        self._attributes = attributes
        self._account_id = account_id
        self._password = password
        self._organization_id = organization_id
        self._admin_contacts = admin_contacts
        self._id = kwargs.pop("issuer_id", None)
        self._vault_id = parse_key_vault_id(self._id)

    def __repr__(self) -> str:
        return f"<CertificateIssuer [{self.id}]>"[:1024]

    @classmethod
    def _from_issuer_bundle(cls, issuer_bundle: models.IssuerBundle) -> "CertificateIssuer":
        admin_contacts = []
        admin_details = issuer_bundle.organization_details.admin_details if issuer_bundle.organization_details else None
        if admin_details:
            # pylint:disable=protected-access
            for admin_detail in admin_details:
                admin_contacts.append(AdministratorContact._from_admin_detail(admin_detail))
        return cls(
            provider=IssuerProperties._from_issuer_item(issuer_bundle).provider,  # pylint: disable=protected-access
            attributes=issuer_bundle.attributes,
            account_id=issuer_bundle.credentials.account_id if issuer_bundle.credentials else None,
            password=issuer_bundle.credentials.password if issuer_bundle.credentials else None,
            organization_id=issuer_bundle.organization_details.id if issuer_bundle.organization_details else None,
            admin_contacts=admin_contacts,
            issuer_id=issuer_bundle.id,
        )

    @property
    def id(self) -> Optional[str]:
        """The issuer ID.

        :returns: The issuer ID.
        :rtype: str or None
        """
        return self._id

    @property
    def name(self) -> Optional[str]:
        """The issuer name.

        :returns: The issuer name.
        :rtype: str or None
        """
        # Issuer name is listed under version under vault_id.
        # This is because the id we pass to parse_key_vault_id has an extra segment, so where most cases the version of
        # the general pattern is certificates/name/version, but here we have certificates/issuers/name/version.
        # Issuers are not versioned.
        return self._vault_id.version

    @property
    def provider(self) -> Optional[str]:
        """The issuer provider.

        :returns: The issuer provider.
        :rtype: str or None
        """
        return self._provider

    @property
    def enabled(self) -> Optional[bool]:
        """Whether the certificate is enabled or not.

        :returns: True if the certificate is enabled; False otherwise.
        :rtype: bool or None
        """
        return self._attributes.enabled if self._attributes else None

    @property
    def created_on(self) -> Optional[datetime]:
        """The datetime when the certificate is created.

        :returns: The datetime when the certificate is created.
        :rtype: ~datetime.datetime or None
        """
        return self._attributes.created if self._attributes else None

    @property
    def updated_on(self) -> Optional[datetime]:
        """The datetime when the certificate was last updated.

        :returns: The datetime when the certificate was last updated.
        :rtype: ~datetime.datetime or None
        """
        return self._attributes.updated if self._attributes else None

    @property
    def account_id(self) -> Optional[str]:
        """The username / account name / account id.

        :returns: The username / account name / account id.
        :rtype: str or None
        """
        return self._account_id

    @property
    def password(self) -> Optional[str]:
        """The password / secret / account key.

        :returns: The password / secret / account key.
        :rtype: str or None
        """
        return self._password

    @property
    def organization_id(self) -> Optional[str]:
        """The issuer organization ID.

        :returns: The issuer organization ID.
        :rtype: str or None
        """
        return self._organization_id

    @property
    def admin_contacts(self) -> Optional[List[AdministratorContact]]:
        """Contact details of the organization administrator(s) of this issuer.

        :returns: Contact details of the organization administrator(s) of this issuer.
        :rtype: list[~azure.keyvault.certificates.AdministratorContact] or None
        """
        return self._admin_contacts


class LifetimeAction(object):
    """Action and its trigger that will be performed by certificate Vault over the lifetime of a certificate.

    :param action: The type of the action. For valid values, see CertificatePolicyAction
    :type action: str or ~azure.keyvault.certificates.CertificatePolicyAction or None
    :param lifetime_percentage: Percentage of lifetime at which to trigger. Value should be between 1 and 99.
    :type lifetime_percentage: int or None
    :param days_before_expiry: Days before expiry to attempt renewal. Value should be between 1 and
        `validity_in_months` multiplied by 27. I.e., if validity_in_months is 36, then value should be between 1 and 972
        (36 * 27).
    :type days_before_expiry: int or None
    """

    def __init__(
        self,
        action: Union[str, CertificatePolicyAction, None],
        lifetime_percentage: Optional[int] = None,
        days_before_expiry: Optional[int] = None,
    ) -> None:
        self._lifetime_percentage = lifetime_percentage
        self._days_before_expiry = days_before_expiry
        self._action = action

    def __repr__(self) -> str:
        result = (
            f"LifetimeAction(action={self.action}, lifetime_percentage={self.lifetime_percentage}, "
            + f"days_before_expiry={self.days_before_expiry})"
        )
        return result[:1024]

    @property
    def lifetime_percentage(self) -> Optional[int]:
        """Percentage of lifetime at which to trigger.

        :returns: Percentage of lifetime at which to trigger.
        :rtype: int or None
        """
        return self._lifetime_percentage

    @property
    def days_before_expiry(self) -> Optional[int]:
        """Days before expiry to attempt renewal.

        :returns: Days before expiry to attempt renewal.
        :rtype: int or None
        """
        return self._days_before_expiry

    @property
    def action(self) -> Union[str, CertificatePolicyAction, None]:
        """The type of action that will be executed; see :class:`~azure.keyvault.certificates.CertificatePolicyAction`.

        :returns: The type of action that will be executed; see
            :class:`~azure.keyvault.certificates.CertificatePolicyAction`.
        :rtype: str or ~azure.keyvault.certificates.CertificatePolicyAction or None
        """
        return self._action


class DeletedCertificate(KeyVaultCertificate):
    """A deleted Certificate consisting of its previous ID, attributes, tags, and information on when it will be purged.

    :param properties: Properties of the deleted certificate.
    :type properties: ~azure.keyvault.certificates.CertificateProperties
    :param policy: The management policy of the deleted certificate.
    :type policy: ~azure.keyvault.certificates.CertificatePolicy or None
    :param cer: CER contents of the X509 certificate.
    :type cer: bytearray or None

    :keyword deleted_on: The time when the certificate was deleted, in UTC.
    :paramtype deleted_on: ~datetime.datetime or None
    :keyword recovery_id: The url of the recovery object, used to identify and recover the deleted certificate.
    :paramtype recovery_id: str or None
    :keyword scheduled_purge_date: The time when the certificate is scheduled to be purged, in UTC.
    :paramtype scheduled_purge_date: ~datetime.datetime or None
    """

    def __init__(
        self,
        properties: Optional[CertificateProperties] = None,
        policy: Optional[CertificatePolicy] = None,
        cer: Optional[bytearray] = None,
        **kwargs: Any,
    ) -> None:
        super(DeletedCertificate, self).__init__(properties=properties, policy=policy, cer=cer, **kwargs)
        self._deleted_on = kwargs.get("deleted_on", None)
        self._recovery_id = kwargs.get("recovery_id", None)
        self._scheduled_purge_date = kwargs.get("scheduled_purge_date", None)

    def __repr__(self) -> str:
        return f"<DeletedCertificate [{self.id}]>"[:1024]

    @classmethod
    def _from_deleted_certificate_item(
        cls, deleted_certificate_item: models.DeletedCertificateItem
    ) -> "DeletedCertificate":
        return cls(
            properties=CertificateProperties._from_certificate_item(  # pylint: disable=protected-access
                deleted_certificate_item
            ),
            key_id=None,
            secret_id=None,
            policy=None,
            cer=None,
            deleted_on=deleted_certificate_item.deleted_date,
            recovery_id=deleted_certificate_item.recovery_id,
            scheduled_purge_date=deleted_certificate_item.scheduled_purge_date,
        )

    @classmethod
    def _from_deleted_certificate_bundle(
        cls, deleted_certificate_bundle: models.DeletedCertificateBundle
    ) -> "DeletedCertificate":
        # pylint:disable=protected-access
        return cls(
            properties=CertificateProperties._from_certificate_bundle(deleted_certificate_bundle),
            key_id=deleted_certificate_bundle.kid,
            secret_id=deleted_certificate_bundle.sid,
            policy=CertificatePolicy._from_certificate_policy_bundle(deleted_certificate_bundle.policy),
            cer=deleted_certificate_bundle.cer,  # type: ignore
            deleted_on=deleted_certificate_bundle.deleted_date,
            recovery_id=deleted_certificate_bundle.recovery_id,
            scheduled_purge_date=deleted_certificate_bundle.scheduled_purge_date,
        )

    @property
    def deleted_on(self) -> Optional[datetime]:
        """The datetime when the certificate was deleted.

        :returns: The datetime when the certificate was deleted.
        :rtype: ~datetime.datetime or None
        """
        return self._deleted_on

    @property
    def recovery_id(self) -> Optional[str]:
        """The URL of the recovery object, used to identify and recover the deleted certificate.

        :returns: The URL of the recovery object, used to identify and recover the deleted certificate.
        :rtype: str or None
        """
        return self._recovery_id

    @property
    def scheduled_purge_date(self) -> Optional[datetime]:
        """The datetime when the certificate is scheduled to be purged.

        :returns: The datetime when the certificate is scheduled to be purged.
        :rtype: ~datetime.datetime or None
        """
        return self._scheduled_purge_date
