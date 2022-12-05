from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework_mongoengine import viewsets

from geographic_services.provider.models import Provider
from geographic_services.provider.serializers import ProviderSerializer


class ProviderView(viewsets.ModelViewSet):

    serializer_class = ProviderSerializer
    lookup_field = 'provider_id'

    def get_queryset(self):
        return Provider.objects.all()

    @method_decorator(cache_page(settings.PROVIDER_CACHE_TTL))
    def retrieve(self, *args, **kwargs):
        return super().retrieve(*args, **kwargs)
