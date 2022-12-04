from rest_framework_mongoengine import serializers

from geographic_services.provider.models import Provider


class ProviderSerializer(serializers.DocumentSerializer):

    class Meta:

        model = Provider
        fields = [
            'provider_id',
            'name',
            'email',
            'phone_number',
            'language',
            'currency'
        ]
