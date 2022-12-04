from rest_framework_mongoengine import viewsets

from geographic_services.service_area.models import ServiceArea
from geographic_services.service_area.serializers import ServiceAreaSerializer


class ServiceAreaView(viewsets.ModelViewSet):

    serializer_class = ServiceAreaSerializer
    lookup_field = 'service_area_id'

    def get_queryset(self):
        return ServiceArea.objects.all()
