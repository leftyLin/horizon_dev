from horizon import views
from django.views.generic import TemplateView  # noqa 


class IndexView(views.APIView):
    # A very simple class-based view...
    template_name = 'tltest/network_topology/index.html'

    def get_data(self, request, context, *args, **kwargs):
        # Add data to the context here...
        return context


class Network_TopologyView (TemplateView):
    template_name = 'tltest/network_topology/index.html'
