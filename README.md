# netbox-dns-easy

## Installation
1. Activate your netbox venv (`source .../netbox/venv/bin/activate`)
1. Run `pip install git+https://github.com/dchiquito/netbox-dns-easy`
1. In your `netbox/configurations.py`, add `"netbox_dns_easy"` to the `PLUGINS` list.

## Development Installation
1. Clone the repostory.
1. Activate your netbox venv (`source .../netbox/venv/bin/activate`)
1. Run `pip install -e .../netbox-dns-easy`
1. In your `netbox/configurations.py`, add `"netbox_dns_easy"` to the `PLUGINS` list.

## Formatting
```
poetry run ruff check --fix
```
