import json

import mongoengine
import pytest
from rest_framework.test import APIRequestFactory

from geographic_services.provider.views import ProviderView


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
