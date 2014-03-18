from django.utils.translation import ugettext_lazy as _

import horizon

class MyPanels(horizon.PanelGroup):
    slug = "MyPanels"
    name = _("MyPanels")
    panels = ('network_topology',)

class tltest(horizon.Dashboard):
    name = _("tltest")
    slug = "tltest"
    panels = (MyPanels, )  # Add your panels here.
    default_panel = 'network_topology'  # Specify the slug of the dashboard's default panel.

horizon.register(tltest)
