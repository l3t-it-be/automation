import allure
import requests

from requests_library.restful_api.endpoints.base_api import BaseAPI
from requests_library.restful_api.models.objects_models import (
    DeleteResponseModel,
)


class DeleteObject(BaseAPI):
    def __init__(self, object_id):
        super().__init__()
        self.url = self.base_url + f'/objects/{object_id}'

    @allure.step('Send request to delete object by its ID')
    def delete_response(self):
        self.response = requests.delete(self.url)
        self.status_code = self.response.status_code
        self.json = self.response.json()

    @allure.step('Assert successful deletion message')
    def assert_delete_message(self, object_id):
        self.object_data = DeleteResponseModel(**self.json)
        expected_message = f'Object with id = {object_id} has been deleted.'

        assert (
            self.object_data.message == expected_message
        ), f'Expected message "{expected_message}", but got "{self.object_data.message}"'
