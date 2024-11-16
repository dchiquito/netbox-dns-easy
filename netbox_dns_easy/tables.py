import django_tables2 as tables
from django.utils.translation import gettext_lazy as _

from netbox.tables import NetBoxTable, columns
from dcim.models import Device


class DeviceDomainTable(NetBoxTable):
    name = tables.Column(linkify=True)
    status = columns.ChoiceFieldColumn(
        verbose_name=_("Status"),
    )

    class Meta(NetBoxTable.Meta):
        model = Device
        fields = (
            "pk",
            "id",
            "name",
            "status",
            "tenant",
            "site",
            "primary_ip",
            "dns_name",
        )
        default_columns = ("name", "status", "tenant",
                           "site", "primary_ip", "dns_name")
