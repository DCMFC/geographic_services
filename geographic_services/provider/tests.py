import json

import pytest

from geographic_services.provider.views import ProviderView


def test_should_save_new_provider_successfully(
    client, provider_payload, db_setup
):
    view = ProviderView.as_view({'post': 'create'})
    request = client.post(
        '/v1/providers',
        json.dumps(provider_payload),
        content_type='application/json'
    )
    response = view(request)

    assert response.status_code == 201
    del response.data['provider_id']
    assert response.data == provider_payload


@pytest.mark.parametrize('field, invalid_value', [
    ('name', None),
    ('email', 'invalid-email'),
    ('phone_number', None),
    ('language', None),
    ('currency', None)
])
def test_post_should_return_bad_request_when_payload_invalid(
   field, invalid_value, client, provider_payload, db_setup
):
    provider_payload[field] = invalid_value
    view = ProviderView.as_view({'post': 'create'})
    request = client.post(
        '/v1/providers',
        json.dumps(provider_payload),
        content_type='application/json'
    )
    response = view(request)
    assert response.status_code == 400


def test_put_should_update_provider_successfully(
    client, provider_payload, db_setup, saved_provider
):
    provider_id = saved_provider['provider_id']
    provider_payload['email'] = 'new_email@example.com'

    view = ProviderView.as_view({'put': 'update'})
    request = client.put(
        f'/v1/providers/{provider_id}',
        json.dumps(provider_payload),
        content_type='application/json'
    )
    response = view(request, provider_id=provider_id)

    assert response.status_code == 200
    assert response.data['email'] == 'new_email@example.com'


@pytest.mark.parametrize('field, invalid_value', [
    ('name', None),
    ('email', 'invalid-email'),
    ('phone_number', None),
    ('language', None),
    ('currency', None)
])
def test_put_should_return_bad_request_when_payload_is_invalid(
    field,
    invalid_value,
    client,
    provider_payload,
    db_setup,
    saved_provider
):
    provider_id = saved_provider['provider_id']
    provider_payload[field] = invalid_value

    view = ProviderView.as_view({'put': 'update'})
    request = client.put(
        f'/v1/providers/{provider_id}',
        json.dumps(provider_payload),
        content_type='application/json'
    )
    response = view(request, provider_id=provider_id)

    assert response.status_code == 400


def test_put_should_return_not_found(
    client, provider_payload, db_setup
):
    view = ProviderView.as_view({'put': 'update'})
    request = client.put(
        '/v1/providers/invalid-id',
        json.dumps(provider_payload),
        content_type='application/json'
    )
    response = view(request, provider_id='invalid-id')

    assert response.status_code == 404


def test_patch_should_update_provider_successfully(
    client, db_setup, saved_provider, provider_payload
):
    provider_id = saved_provider['provider_id']

    view = ProviderView.as_view({'patch': 'update'})
    provider_payload['email'] = 'new_email@example.com'
    request = client.patch(
        f'/v1/providers/{provider_id}',
        json.dumps(provider_payload),
        content_type='application/json'
    )
    response = view(request, provider_id=provider_id)
    assert response.status_code == 200
    assert response.data['email'] == 'new_email@example.com'


@pytest.mark.parametrize('field, invalid_value', [
    ('name', None),
    ('email', 'invalid-email'),
    ('phone_number', None),
    ('language', None),
    ('currency', None)
])
def test_patch_should_return_bad_request_when_payload_is_invalid(
    field,
    invalid_value,
    client,
    db_setup,
    saved_provider
):
    provider_id = saved_provider['provider_id']

    view = ProviderView.as_view({'patch': 'update'})
    request = client.patch(
        f'/v1/providers/{provider_id}',
        json.dumps({field: invalid_value}),
        content_type='application/json'
    )
    response = view(request, provider_id=provider_id)

    assert response.status_code == 400


def test_patch_should_return_not_found(
    client, provider_payload, db_setup
):
    view = ProviderView.as_view({'patch': 'update'})
    request = client.patch(
        '/v1/providers/invalid-id',
        json.dumps(provider_payload),
        content_type='application/json'
    )
    response = view(request, provider_id='invalid-id')

    assert response.status_code == 404


def test_delete_should_remove_provider_successfully(
    client, db_setup, saved_provider
):
    provider_id = saved_provider['provider_id']

    view = ProviderView.as_view({'delete': 'destroy'})
    request = client.delete(
        f'/v1/providers/{provider_id}',
        content_type='application/json'
    )
    response = view(request, provider_id=provider_id)
    assert response.status_code == 204


def test_delete_should_return_not_found(
    client, db_setup
):
    view = ProviderView.as_view({'delete': 'destroy'})
    request = client.delete(
        '/v1/providers/invalid-id',
        content_type='application/json'
    )
    response = view(request, provider_id='invalid-id')
    assert response.status_code == 404


def test_list_should_retrieve_all_providers_successfully(
    client, db_setup, saved_list_providers
):
    view = ProviderView.as_view({'get': 'list'})
    request = client.get(
        '/v1/providers',
        content_type='application/json'
    )
    response = view(request)
    assert response.status_code == 200
    content = response.render().content
    content = json.loads(content)
    assert content['count'] == 15


def test_list_should_retrieve_empty_result_successfully(
    client, db_setup
):
    view = ProviderView.as_view({'get': 'list'})
    request = client.get(
        '/v1/providers',
        content_type='application/json'
    )
    response = view(request)
    assert response.status_code == 200
    content = response.render().content
    content = json.loads(content)
    assert content['count'] == 0


def test_get_should_retrieve_provider_successfully(
    client, db_setup, saved_provider
):
    provider_id = saved_provider['provider_id']

    view = ProviderView.as_view({'get': 'retrieve'})
    request = client.get(
        f'/v1/providers/{provider_id}',
        content_type='application/json'
    )
    response = view(request, provider_id=provider_id)
    assert response.status_code == 200
    content = response.render().content
    content = json.loads(content)
    assert content == saved_provider


def test_get_should_return_not_found(
    client, db_setup
):
    view = ProviderView.as_view({'get': 'retrieve'})
    request = client.get(
        '/v1/providers/invalid-id',
        content_type='application/json'
    )
    response = view(request, provider_id='invalid-id')
    assert response.status_code == 404
