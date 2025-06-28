import allure
import requests

from requests_library.restful_api.endpoints.base_api import BaseAPI


class UpdateObject(BaseAPI):
    def __init__(self, object_id):
        super().__init__()
        self.url = self.base_url + f'/objects/{object_id}'

    @allure.step('Send request to update object info by its ID')
    def put_response(self, data):
        self.response = requests.put(self.url, json=data)
        self.status_code = self.response.status_code
        self.json = self.response.json()
