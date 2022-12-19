# Nautobot Secrets Providers Changelog

## v1.3.1 (????-??-??)

### Added

- [] Extra tab on secret detail view to check if the secret can be read if Nautobot Version is greater than 1.4.

## v1.3.0 (2022-08-29)

### Added

- [#32](https://github.com/nautobot/nautobot-plugin-secrets-providers/issues/32) Add support for skipping certificate validation when connecting to HashiCorp Vault.
- [#34](https://github.com/nautobot/nautobot-plugin-secrets-providers/issues/34) Add support for alternate authentication to HashiCorp Vault via AWS and Kubernetes authentication methods.
- [#38](https://github.com/nautobot/nautobot-plugin-secrets-providers/pull/38) Add support for Python 3.10.
- [#40](https://github.com/nautobot/nautobot-plugin-secrets-providers/issues/40) Add `default_mount_point` config option for HashiCorp Vault.

### Changed

- [#42](https://github.com/nautobot/nautobot-plugin-secrets-providers/issues/42) Now requires python-tss-sdk version v1.2 or later

### Fixed

- [#31](https://github.com/nautobot/nautobot-plugin-secrets-providers/issues/31) Fixed NameError at startup when installed as `nautobot_secrets_providers[thycotic]`, i.e. without HashiCorp Vault support.
- [#37](https://github.com/nautobot/nautobot-plugin-secrets-providers/pull/37) Various fixes and improvements to the development environment.

### Removed

- [#38](https://github.com/nautobot/nautobot-plugin-secrets-providers/pull/38) - Dropped support for end-of-life Python 3.6

## v1.2.0 (2022-05-25)

### Added

- [#8](https://github.com/nautobot/nautobot-plugin-secrets-providers/issues/8) Add support for authentication to HashiCorp Vault via AppRole as an alternative to token authentication
- [#23](https://github.com/nautobot/nautobot-plugin-secrets-providers/issues/23) Add support for non-default HashiCorp Vault mountpoints

## v1.1.0 (2022-03-10)

### Added

- [#21](https://github.com/nautobot/nautobot-plugin-secrets-providers/issues/21) Add Thycotic Secret Server plugin
  **Requires Python 3.7 or greater**

## v1.0.1 (2022-01-06)

### Fixed

- [#17](https://github.com/nautobot/nautobot-plugin-secrets-providers/issues/17) Fixed `ModuleNotFoundError` when not installing AWS dependencies

## v1.0.0 (2021-12-22)

This is the initial release of Nautobot Secrets Providers that includes support for basic key-value secrets AWS Secrets Manager and HashiCorp Vault. Please see [README.md](./README.md) for more information.
