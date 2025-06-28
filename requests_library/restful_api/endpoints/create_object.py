import allure
import requests

from requests_library.restful_api.endpoints.base_api import BaseAPI


class CreateObject(BaseAPI):
    def __init__(self):
        super().__init__()
        self.url = self.base_url + '/objects'

    @allure.step('Send request to create object')
    def post_response(self, data):
        self.response = requests.post(self.url, json=data)
        self.json = self.response.json()
        self.status_code = self.response.status_code

    @allure.step('Get created object ID')
    def get_object_id(self):
        return self.object_data.id
