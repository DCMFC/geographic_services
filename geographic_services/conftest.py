import json

import mongoengine
import pytest
from rest_framework.test import APIRequestFactory

from geographic_services.provider.views import ProviderView
from geographic_services.service_area.views import ServiceAreaView


@pytest.fixture
def client():
    client = APIRequestFactory()
    return client


@pytest.fixture
def db_setup():
    db = mongoengine.connect(
        host='mongomock://127.0.0.1:27017/geographic_services'
    )
    yield db
    mongoengine.disconnect()


@pytest.fixture
def provider_payload():
    return {
        'name': 'provider 1',
        'email': 'user@example.com',
        'phone_number': '5511999999999',
        'language': 'en-us',
        'currency': 'us'
    }


@pytest.fixture
def service_area_payload():
    return {
        'name': 'New service area',
        'price': '10.00',
        'geographic_area': {
            'type': 'Polygon',
            'coordinates': [[
                [121.00380420684814, 14.515791721361213],
                [121.00728034973145, 14.513465165268554],
                [121.00946903228758, 14.510307657168987],
                [121.01315975189209, 14.512592700428515],
                [121.00745201110838, 14.51811825299417],
                [121.00380420684814, 14.515791721361213]
            ]]
        },
        'provider_name': 'Provider 1'
    }


@pytest.fixture
def saved_provider(client, provider_payload):
    view = ProviderView.as_view({'post': 'create'})
    request = client.post(
        '/v1/providers',
        json.dumps(provider_payload),
        content_type='application/json'
    )
    return view(request).data


@pytest.fixture
def saved_list_providers(client, provider_payload):
    for i in range(15):
        provider_payload['name'] = f'Provider {str(i)}'
        view = ProviderView.as_view({'post': 'create'})
        request = client.post(
            '/v1/providers',
            json.dumps(provider_payload),
            content_type='application/json'
        )
        view(request)


@pytest.fixture
def saved_service_area(client, service_area_payload):
    view = ServiceAreaView.as_view({'post': 'create'})
    request = client.post(
        '/v1/service_areas',
        json.dumps(service_area_payload),
        content_type='application/json'
    )
    return view(request).data


@pytest.fixture
def saved_list_service_area(client, service_area_payload):
    for i in range(15):
        service_area_payload['name'] = f'Service Area {str(i)}'
        view = ServiceAreaView.as_view({'post': 'create'})
        request = client.post(
            '/v1/service_areas',
            json.dumps(service_area_payload),
            content_type='application/json'
        )
        view(request)
