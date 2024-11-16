from django.db.models import F
from dcim.models import Device
from netbox.views import generic
from netbox_dns.models import Record

from . import forms, tables


class DeviceDomainsView(generic.ObjectListView):
    # TODO start with managed records and work back to the Device
    # Record.objects.filter(managed=True)
    # .ipam_ip_address.assigned_object.parent_object
    queryset = Device.objects.all().annotate(dns_name=F("primary_ip4__dns_name"))
    table = tables.DeviceDomainTable
