from django.conf.urls.defaults import patterns  # noqa
from django.conf.urls.defaults import url  # noqa

#from .views import IndexView
from openstack_dashboard.dashboards.tltest.network_topology import views

urlpatterns = patterns(
    'openstack_dashboard.dashboards.tltest.network_topology.views',
    url(r'^$', views.Network_TopologyView.as_view(), name='index'),
    #url(r'^$', IndexView.as_view(), name='index'),
)
