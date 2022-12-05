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

    @extend_schema(parameters=[
        OpenApiParameter(
            name='latitude', location=OpenApiParameter.QUERY, required=True
        ),
        OpenApiParameter(
            name='longitude', location=OpenApiParameter.QUERY, required=True
        )
    ])
    @action(
        methods=['get'], url_path='list_point_intersections', detail=False
    )
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
