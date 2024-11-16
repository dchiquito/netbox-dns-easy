from django.urls import path
from . import views

urlpatterns = (
    path(
        "device-domains/", views.DeviceDomainsView.as_view(), name="devicedomains_list"
    ),
)
