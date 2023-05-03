from assertions.assertions import Assertions
from pages.http_methods import HttpMethod
from const.const import *


HOST = 'https://cloud-api.yandex.net'
PATH = '/v1/disk/resources'

class YandexDisk(HttpMethod):

    def create_folder(self):
        print('\nPUT /v1/disk/resources - создание новой папки')
        response = self.put(HOST + PATH,
                            params=params_for_create_folder)
        Assertions.assert_status_code(response, 201)
        Assertions.assert_params_in_json(
            response, expected_params_of_response_create_folder)
        Assertions.assert_value_in_json(response, "название папки", folder_name,
                                        response.url[-10:])

    def get_folder(self):
        print('\nGET /v1/disk/resources - проверка наличия созданной папки')
        response = self.get(HOST + PATH,
                            params=params_for_create_folder)
        Assertions.assert_status_code(response, 200)

    def delete_folder(self):
        print('\nDELETE /v1/disk/resources - удаление созданной папки')
        response = self.delete(HOST + PATH,
                            params=params_for_create_folder)
        Assertions.assert_status_code(response, 204)

    def get_deleted_folder(self):
        print('\nGET /v1/disk/resources - проверка наличия удаленной папки')
        response = self.get(HOST + PATH,
                            params=params_for_create_folder)
        Assertions.assert_status_code(response, 404)
