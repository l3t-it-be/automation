import pytest

from requests_library.restful_api.endpoints.create_object import CreateObject
from requests_library.restful_api.endpoints.delete_object import DeleteObject
from requests_library.restful_api.endpoints.get_object import GetObject
from requests_library.restful_api.endpoints.update_object import UpdateObject
from requests_library.restful_api.models.objects_models import (
    RequestObjectModel,
)
from requests_library.restful_api.test_data.objects_data import (
    create_data,
    update_data,
)


@pytest.mark.crud
@pytest.mark.regression
class TestObjects:
    @pytest.mark.smoke
    @pytest.mark.create
    @pytest.mark.parametrize(
        'test_data',
        create_data,
        ids=[f'Create object: {data["name"]}' for data in create_data],
    )
    def test_create_new_object(self, test_data):
        create_object_api = CreateObject()
        create_object_data = RequestObjectModel(**test_data).model_dump(
            by_alias=True
        )
        create_object_api.post_response(create_object_data)

        create_object_api.assert_response_is_200()
        create_object_api.assert_object_name(create_object_data['name'])
        create_object_api.assert_object_data(create_object_data['data'])

    @pytest.mark.smoke
    @pytest.mark.get
    def test_get_object(self, object_id):
        get_object_api = GetObject(object_id)
        get_object_api.get_response()

        get_object_api.assert_response_is_200()
        get_object_api.assert_object_id(object_id)

    @pytest.mark.update
    @pytest.mark.parametrize(
        'test_data',
        update_data,
        ids=[f'Update to: {data["name"]}' for data in update_data],
    )
    def test_update_object(self, object_id, test_data):
        update_object_api = UpdateObject(object_id)
        update_object_data = RequestObjectModel(**test_data).model_dump(
            by_alias=True
        )
        update_object_api.put_response(update_object_data)

        update_object_api.assert_response_is_200()
        update_object_api.assert_object_id(object_id)
        update_object_api.assert_object_name(update_object_data['name'])
        update_object_api.assert_object_data(update_object_data['data'])

    @pytest.mark.smoke
    @pytest.mark.delete
    def test_delete_object(self, object_id):
        delete_object_api = DeleteObject(object_id)
        delete_object_api.delete_response()
        delete_object_api.assert_response_is_200()
        delete_object_api.assert_delete_message(object_id)

        get_object_api = GetObject(object_id)
        get_object_api.get_response()
        get_object_api.assert_response_is_404()
        get_object_api.assert_error_message(object_id)
