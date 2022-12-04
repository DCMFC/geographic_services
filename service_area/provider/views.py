from rest_framework_mongoengine import viewsets

from service_area.provider.models import Provider
from service_area.provider.serializers import ProviderSerializer


class ProviderView(viewsets.ModelViewSet):

    serializer_class = ProviderSerializer
    lookup_field = 'provider_id'

    def get_queryset(self):
        return Provider.objects.all()
