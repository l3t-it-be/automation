import allure
import requests

from requests_library.restful_api.endpoints.base_api import BaseAPI
from requests_library.restful_api.models.objects_models import (
    ErrorResponseModel,
)


class GetObject(BaseAPI):
    def __init__(self, object_id):
        super().__init__()
        self.url = self.base_url + f'/objects/{object_id}'

    @allure.step('Send request to get object info by its ID')
    def get_response(self):
        self.response = requests.get(self.url)
        self.status_code = self.response.status_code
        self.json = self.response.json()

    @allure.step('Assert error message for unexisting object')
    def assert_error_message(self, object_id):
        self.object_data = ErrorResponseModel(**self.json)
        expected_message = f'Oject with id={object_id} was not found.'

        assert (
            self.object_data.error == expected_message
        ), f'Expected message "{expected_message}", but got "{self.object_data.error}"'
