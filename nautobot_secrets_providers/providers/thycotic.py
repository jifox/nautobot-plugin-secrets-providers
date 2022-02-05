"""Secrets Provider for Thycotic Secret Server."""

from django import forms
from django.conf import settings

try:
    import hvac
except ImportError:
    hvac = None

from nautobot.utilities.forms import BootstrapMixin
from nautobot.extras.secrets import exceptions, SecretsProvider


__all__ = ("ThycoticSecretServerSecretsProvider",)


class ThycoticSecretServerSecretsProvider(SecretsProvider):
    """A secrets provider for Thycotic Secret Server."""

    slug = "thycotic-tss"
    name = "Thycotic Secret Server"
    is_available = hvac is not None

    class ParametersForm(BootstrapMixin, forms.Form):
        """Required parameters for Thycotic Secret Server."""

        path = forms.CharField(
            required=True,
            help_text="The path to the Thycotic Secret Server secret",
        )
        key = forms.CharField(
            required=True,
            help_text="The key of the Thycotic Secret Server secret",
        )

    @classmethod
    def get_value_for_secret(cls, secret, obj=None, **kwargs):
        """Return the value stored under the secret’s key in the secret’s path."""
        # This is only required for Thycotic Secret Server therefore not defined in
        # `required_settings` for the plugin config.
        plugin_settings = settings.PLUGINS_CONFIG["nautobot_secrets_providers"]
        if "hashicorp_vault" not in plugin_settings:
            raise exceptions.SecretProviderError(secret, cls, "Thycotic Secret Server is not configured!")

        vault_settings = plugin_settings["hashicorp_vault"]
        if "url" not in vault_settings or "token" not in vault_settings:
            raise exceptions.SecretProviderError(secret, cls, "Thycotic Secret Server is not configured!")

        # Try to get parameters and error out early.
        parameters = secret.rendered_parameters(obj=obj)
        try:
            secret_path = parameters["path"]
            secret_key = parameters["key"]
        except KeyError as err:
            msg = f"The secret parameter could not be retrieved for field {err}"
            raise exceptions.SecretParametersError(secret, cls, msg) from err

        # Get the client and attempt to retrieve the secret.
        client = hvac.Client(url=vault_settings["url"], token=vault_settings["token"])
        try:
            response = client.secrets.kv.read_secret(path=secret_path)
        except hvac.exceptions.InvalidPath as err:
            raise exceptions.SecretValueNotFoundError(secret, cls, str(err)) from err

        # Retrieve the value using the key or complain loudly.
        try:
            return response["data"]["data"][secret_key]
        except KeyError as err:
            msg = f"The secret value could not be retrieved using key {err}"
            raise exceptions.SecretValueNotFoundError(secret, cls, msg) from err
