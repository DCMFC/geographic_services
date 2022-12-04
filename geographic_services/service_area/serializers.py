from rest_framework_mongoengine import serializers

from geographic_services.service_area.models import ServiceArea


class ServiceAreaSerializer(serializers.DocumentSerializer):

    class Meta:

        model = ServiceArea
        fields = [
            'service_area_id',
            'name',
            'price',
            'geographic_area',
            'provider_name'
        ]
