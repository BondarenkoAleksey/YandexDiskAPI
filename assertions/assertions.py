from requests import Response


class Assertions:

    """Проверка статус-кода"""

    def assert_status_code(self: Response, expected_status_code):
        assert self.status_code == expected_status_code, \
            f'FAIL! Статус-код {self.status_code}.' \
            f'{self.json()}'
        print(f'Успешно! Статус-код запроса ниже: {self.status_code}')
        print(self.url)

    """Проверка параметров в JSON"""

    def assert_params_in_json(self: Response, expected_params):

        json_params = list(self.json().keys())
        not_matches = [i for i in json_params if i
                               not in expected_params]
        not_matches2 = [i for i in expected_params if i
                                not in json_params]
        assert not_matches == not_matches2 == [], f'FAIL! Ожидаемые параметры и фактические ' \
                                                  f'не совпали на {not_matches}'
        print(f"Полученные в JSON названия параметров совпали с "
                      f"ожидаемыми из списка {expected_params}")

    """Проверка соответствия фактического значения параметра ожидаемому"""
    def assert_value_in_json(
            self: Response, expected_param, expected_value, fact_value):
        assert fact_value == expected_value, \
            f'FAIL! Ожидаемое и фактическое значения' \
            f' параметра "{expected_param}" не совпали' \
            f' fact_value = {fact_value}, expected_value = {expected_value}'
        print(f"Полученное значение параметра \"{expected_param}\","
              f" равное {fact_value}, совпадает с ожидаемым.")

