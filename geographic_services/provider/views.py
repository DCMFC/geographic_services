from rest_framework_mongoengine import viewsets

from geographic_services.provider.models import Provider
from geographic_services.provider.serializers import ProviderSerializer


class ProviderView(viewsets.ModelViewSet):

    serializer_class = ProviderSerializer
    lookup_field = 'provider_id'

    def get_queryset(self):
        return Provider.objects.all()
