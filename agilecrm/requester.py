import requests

from agilecrm.responses import SuccessResponse, ErrorResponse, NonSuccessResponse


class Requester:
    def __init__(self, domain, email, api_key):
        self.base_url = "https://{domain}.agilecrm.com/dev/api/".format(domain=domain)
        self.auth = (email, api_key)
        self.headers = {
            'Accept': 'application/json',
            'content-type': 'application/json',
        }

    def get(self, url, params=None):
        url = self.base_url + url

        response = requests.get(url, auth=self.auth, headers=self.headers, params=params)

        if not response.ok:
            return ErrorResponse(status=response.status_code, text=response.text)

        if not response.status_code == 200:
            return NonSuccessResponse(status=response.status_code, text=response.text)

        return SuccessResponse(data=response.json())

    def post(self, url, data):
        url = self.base_url + url

        response = requests.post(url, json=data, auth=self.auth, headers=self.headers)

        if not response.ok:
            return ErrorResponse(status=response.status_code, text=response.text)

        if not response.status_code == 200:
            return NonSuccessResponse(status=response.status_code, text=response.text)

        return SuccessResponse(data=response.json())

    def put(self, url, data):
        url = self.base_url + url

        response = requests.put(url, json=data, auth=self.auth, headers=self.headers)

        if not response.ok:
            return ErrorResponse(status=response.status_code, text=response.text)

        if not response.status_code == 200:
            return NonSuccessResponse(status=response.status_code, text=response.text)

        return SuccessResponse(data=response.json())

    def delete(self, url):
        url = self.base_url + url

        response = requests.delete(url, auth=self.auth, headers=self.headers)

        if not response.ok:
            return ErrorResponse(status=response.status_code, text=response.text)

        if not response.status_code == 204:
            return ErrorResponse(status=response.status_code, text=response.text)

        return SuccessResponse(text=response.text)
