from django.db.models import F
from netbox.views import generic
from netbox_dns.models import Record

from . import tables


class DeviceDomainsView(generic.ObjectListView):
    # TODO start with managed records and work back to the Device
    # Record.objects.filter(managed=True)
    # .ipam_ip_address.assigned_object.parent_object
    # address_records = ip_address.netbox_dns_records.all()
    # queryset = Device.objects.all().annotate(dns_name=F("primary_ip4__dns_name"))
    def get_queryset(self, request):
        # ip_addresses = (
        #     row[0]
        #     for row in Record.objects.filter(managed=True).values_list(
        #         "ipam_ip_address"
        #     )
        # )

        return (
            Record.objects.filter(managed=True)
            .exclude(ipam_ip_address=None)
            .alias(device=F("ipam_ip_address__interface__device"))
            .annotate(
                dns_name=F("ipam_ip_address__dns_name"),
                ipam_ip_pk=F("ipam_ip_address__pk"),
                ipam_ip=F("ipam_ip_address__address"),
                device_pk=F("ipam_ip_address__interface__device__pk"),
                device_name=F("ipam_ip_address__interface__device__name"),
                device_status=F("ipam_ip_address__interface__device__status"),
                device_tenant_pk=F("ipam_ip_address__interface__device__tenant__pk"),
                device_tenant=F("ipam_ip_address__interface__device__tenant__name"),
                device_site_pk=F("ipam_ip_address__interface__device__site__pk"),
                device_site=F("ipam_ip_address__interface__device__site__name"),
            )
        )

    table = tables.DeviceDomainTable
