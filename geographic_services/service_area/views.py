from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_mongoengine import viewsets

from geographic_services.service_area.models import ServiceArea
from geographic_services.service_area.serializers import ServiceAreaSerializer


class ServiceAreaView(viewsets.ModelViewSet):

    serializer_class = ServiceAreaSerializer
    lookup_field = 'service_area_id'

    def get_queryset(self):
        return ServiceArea.objects.all()

    @method_decorator(cache_page(settings.SERVICE_AREA_CACHE_TTL))
    def retrieve(self, *args, **kwargs):
        return super().retrieve(*args, **kwargs)

    @extend_schema(parameters=[
        OpenApiParameter(
            name='latitude', location=OpenApiParameter.QUERY, required=True
        ),
        OpenApiParameter(
            name='longitude', location=OpenApiParameter.QUERY, required=True
        )
    ])
    @action(methods=['get'], url_path='point_intersections', detail=False)
    @method_decorator(cache_page(settings.SERVICE_AREA_CACHE_TTL))
    def get_service_areas_intersections(self, request, **kwargs):
        latitude = request.query_params.get('latitude')
        longitude = request.query_params.get('longitude')

        if not latitude or not longitude:
            return Response(
                data='Latitude and longitude are required',
                status=status.HTTP_400_BAD_REQUEST
            )

        service_areas = ServiceArea.objects(
            geographic_area__geo_intersects=[float(latitude), float(longitude)]
        )
        serializer = ServiceAreaSerializer(service_areas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
