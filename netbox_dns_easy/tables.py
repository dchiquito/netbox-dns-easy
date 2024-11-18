import django_tables2 as tables
from django.utils.translation import gettext_lazy as _

from netbox.tables import NetBoxTable, columns
from dcim.models import Device
from netbox_dns.models import Record


class DeviceDomainTable(NetBoxTable):
    ipam_ip = tables.Column(linkify=("ipam:ipaddress", [tables.A("ipam_ip_pk")]))
    device_name = tables.Column(linkify=("dcim:device", [tables.A("device_pk")]))
    device_status = columns.ChoiceFieldColumn(
        verbose_name=_("Status"),
    )
    device_tenant = tables.Column(
        linkify=("tenancy:tenant", [tables.A("device_tenant_pk")])
    )
    device_site = tables.Column(linkify=("dcim:site", [tables.A("device_site_pk")]))

    class Meta(NetBoxTable.Meta):
        model = Record
        fields = (
            # "pk",
            # "id",
            "dns_name",
            "ipam_ip",
            "device_name",
            "device_status",
            "device_tenant",
            "device_site",
        )
        default_columns = (
            "dns_name",
            "ipam_ip",
            "device_name",
            "device_status",
            "device_tenant",
            "device_site",
        )
