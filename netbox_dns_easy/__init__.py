from netbox.plugins import PluginConfig


class NetBoxAccessListsConfig(PluginConfig):
    name = "netbox_dns_easy"
    verbose_name = "Easy DNS for NetBox"
    description = "A simple interface for DNS management in NetBox"
    version = "0.1"
    base_url = "dns-easy"


config = NetBoxAccessListsConfig
