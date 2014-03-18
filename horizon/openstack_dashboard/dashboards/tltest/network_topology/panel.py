from django.utils.translation import ugettext_lazy as _

import horizon
from openstack_dashboard.dashboards.tltest import dashboard


class Network_Topology(horizon.Panel):
    name = _("Network_Topology")
    slug = 'network_topology'
    permissions = ('openstack.services.network', )

dashboard.tltest.register(Network_Topology)
