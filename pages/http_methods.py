import requests

TOKEN = 'token'
headers = {
    'Content-Type': 'application/json',
    'Authorization': TOKEN
}
cookies = ""


class HttpMethod:

    @staticmethod
    def get(url, params=None):
        response = requests.get(url, headers=headers,
                                cookies=cookies, params=params)
        return response

    @staticmethod
    def post(url, payload=None, post_json=None, files=None):
        response = requests.post(url, json=post_json, data=payload,
                                 headers=headers, cookies=cookies, files=files)
        return response

    @staticmethod
    def put(url, payload=None, put_json=None, files=None, params=None):
        response = requests.put(url, json=put_json, data=payload,
                                 headers=headers, cookies=cookies, files=files, params=params)
        return response

    @staticmethod
    def patch(url, payload=None, patch_json=None, files=None):
        response = requests.patch(url, json=patch_json, data=payload,
                                  headers=headers, cookies=cookies, files=files)
        return response

    @staticmethod
    def delete(url, params=None):
        response = requests.delete(url, headers=headers, cookies=cookies, params=params)
        return response