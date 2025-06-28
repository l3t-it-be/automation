import pytest

from requests_library.restful_api.endpoints.create_object import CreateObject
from requests_library.restful_api.endpoints.delete_object import DeleteObject
from requests_library.restful_api.models.objects_models import (
    RequestObjectModel,
)
from requests_library.restful_api.test_data.objects_data import create_data


@pytest.fixture
def object_id():
    create_object_api = CreateObject()
    create_object_data = RequestObjectModel(**create_data[0]).model_dump(
        by_alias=True
    )
    create_object_api.post_response(create_object_data)

    create_object_api.assert_response_is_200()
    create_object_api.assert_object_name(create_object_data['name'])
    create_object_api.assert_object_data(create_object_data['data'])

    id = create_object_api.get_object_id()
    yield id

    delete_object_api = DeleteObject(id)
    delete_object_api.delete_response()
