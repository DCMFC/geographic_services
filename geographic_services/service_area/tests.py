import json

import pytest

from geographic_services.service_area.views import ServiceAreaView


def test_should_save_new_service_area_successfully(
    client, service_area_payload, db_setup
):
    view = ServiceAreaView.as_view({'post': 'create'})
    request = client.post(
        '/v1/service_areas',
        json.dumps(service_area_payload),
        content_type='application/json'
    )
    response = view(request)

    assert response.status_code == 201
    del response.data['service_area_id']
    assert response.data == service_area_payload


@pytest.mark.parametrize('field, invalid_value', [
    ('name', None),
    ('price', 'invalid-value'),
    ('geographic_area', None),
    ('provider_name', None)
])
def test_post_service_area_should_return_bad_request_when_payload_invalid(
   field, invalid_value, client, service_area_payload, db_setup
):
    service_area_payload[field] = invalid_value
    view = ServiceAreaView.as_view({'post': 'create'})
    request = client.post(
        '/v1/service_areas',
        json.dumps(service_area_payload),
        content_type='application/json'
    )
    response = view(request)
    assert response.status_code == 400


def test_put_should_update_service_area_successfully(
    client, service_area_payload, db_setup, saved_service_area
):
    service_area_id = saved_service_area['service_area_id']
    service_area_payload['price'] = '20.50'

    view = ServiceAreaView.as_view({'put': 'update'})
    request = client.put(
        f'/v1/service_areas/{service_area_id}',
        json.dumps(service_area_payload),
        content_type='application/json'
    )
    response = view(request, service_area_id=service_area_id)

    assert response.status_code == 200
    assert response.data['price'] == '20.50'


@pytest.mark.parametrize('field, invalid_value', [
    ('name', None),
    ('price', 'invalid-value'),
    ('geographic_area', None),
    ('provider_name', None)
])
def test_put_service_area_should_return_bad_request_when_payload_is_invalid(
    field,
    invalid_value,
    client,
    service_area_payload,
    db_setup,
    saved_service_area
):
    service_area_id = saved_service_area['service_area_id']
    service_area_payload[field] = invalid_value

    view = ServiceAreaView.as_view({'put': 'update'})
    request = client.put(
        f'/v1/service_areas/{service_area_id}',
        json.dumps(service_area_payload),
        content_type='application/json'
    )
    response = view(request, service_area_id=service_area_id)

    assert response.status_code == 400


def test_put_service_area_should_return_not_found(
    client, service_area_payload, db_setup
):
    view = ServiceAreaView.as_view({'put': 'update'})
    request = client.put(
        '/v1/service_areas/invalid-id',
        json.dumps(service_area_payload),
        content_type='application/json'
    )
    response = view(request, service_area_id='invalid-id')

    assert response.status_code == 404


def test_patch_should_update_service_area_successfully(
    client, db_setup, saved_service_area, service_area_payload
):
    service_area_id = saved_service_area['service_area_id']

    view = ServiceAreaView.as_view({'patch': 'update'})
    service_area_payload['price'] = '30.00'
    request = client.patch(
        f'/v1/service_areas/{service_area_id}',
        json.dumps(service_area_payload),
        content_type='application/json'
    )
    response = view(request, service_area_id=service_area_id)
    assert response.status_code == 200
    assert response.data['price'] == '30.00'


@pytest.mark.parametrize('field, invalid_value', [
    ('name', None),
    ('price', 'invalid-value'),
    ('geographic_area', None),
    ('provider_name', None)
])
def test_patch_service_area_should_return_bad_request_when_payload_is_invalid(
    field,
    invalid_value,
    client,
    db_setup,
    saved_service_area
):
    service_area_id = saved_service_area['service_area_id']

    view = ServiceAreaView.as_view({'patch': 'update'})
    request = client.patch(
        f'/v1/service_areas/{service_area_id}',
        json.dumps({field: invalid_value}),
        content_type='application/json'
    )
    response = view(request, service_area_id=service_area_id)

    assert response.status_code == 400


def test_patch_service_area_should_return_not_found(
    client, service_area_payload, db_setup
):
    view = ServiceAreaView.as_view({'patch': 'update'})
    request = client.patch(
        '/v1/service_areas/invalid-id',
        json.dumps(service_area_payload),
        content_type='application/json'
    )
    response = view(request, service_area_id='invalid-id')

    assert response.status_code == 404


def test_delete_should_remove_service_area_successfully(
    client, db_setup, saved_service_area
):
    service_area_id = saved_service_area['service_area_id']

    view = ServiceAreaView.as_view({'delete': 'destroy'})
    request = client.delete(
        f'/v1/service_areas/{service_area_id}',
        content_type='application/json'
    )
    response = view(request, service_area_id=service_area_id)
    assert response.status_code == 204


def test_delete_service_area_should_return_not_found(
    client, db_setup
):
    view = ServiceAreaView.as_view({'delete': 'destroy'})
    request = client.delete(
        '/v1/service_areas/invalid-id',
        content_type='application/json'
    )
    response = view(request, service_area_id='invalid-id')
    assert response.status_code == 404


def test_list_should_retrieve_all_service_areas_successfully(
    client, db_setup, saved_list_service_area
):
    view = ServiceAreaView.as_view({'get': 'list'})
    request = client.get(
        '/v1/service_areas',
        content_type='application/json'
    )
    response = view(request)
    assert response.status_code == 200
    content = response.render().content
    content = json.loads(content)
    assert content['count'] == 15


def test_list_service_areas_should_retrieve_empty_result_successfully(
    client, db_setup
):
    view = ServiceAreaView.as_view({'get': 'list'})
    request = client.get(
        '/v1/service_areas',
        content_type='application/json'
    )
    response = view(request)
    assert response.status_code == 200
    content = response.render().content
    content = json.loads(content)
    assert content['count'] == 0


def test_get_should_retrieve_service_area_successfully(
    client, db_setup, saved_service_area
):
    service_area_id = saved_service_area['service_area_id']

    view = ServiceAreaView.as_view({'get': 'retrieve'})
    request = client.get(
        f'/v1/service_areas/{service_area_id}',
        content_type='application/json'
    )
    response = view(request, service_area_id=service_area_id)
    assert response.status_code == 200
    content = response.render().content
    content = json.loads(content)
    assert content == saved_service_area


def test_get_service_area_should_return_not_found(
    client, db_setup
):
    view = ServiceAreaView.as_view({'get': 'retrieve'})
    request = client.get(
        '/v1/service_areas/invalid-id',
        content_type='application/json'
    )
    response = view(request, service_area_id='invalid-id')
    assert response.status_code == 404
