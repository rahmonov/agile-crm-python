import requests


class Requester:
    def __init__(self, domain, email, api_key):
        self.base_url = "https://{domain}.agilecrm.com/dev/api/".format(domain=domain)
        self.auth = (email, api_key)
        self.headers = {
            'Accept': 'application/json',
            'content-type': 'application/json',
        }

    def get(self, url):
        url = self.base_url + url

        response = requests.get(url, auth=self.auth, headers=self.headers)

        if not response.ok:
            return {'status_code': response.status_code, 'text': response.text, 'ok': False}

        if not response.status_code == 200:
            return {'status_code': response.status_code, 'text': response.text, 'ok': True}

        return {'status_code': response.status_code, 'data': response.json(), 'ok': True}

    def post(self, url, data):
        url = self.base_url + url

        response = requests.post(url, json=data, auth=self.auth, headers=self.headers)

        if not response.ok:
            return {'status_code': response.status_code, 'text': response.text, 'ok': False}

        if not response.status_code == 200:
            return {'status_code': response.status_code, 'text': response.text, 'ok': True}

        return {'status_code': response.status_code, 'data': response.json(), 'ok': True}

    def put(self, url, data):
        url = self.base_url + url

        response = requests.put(url, json=data, auth=self.auth, headers=self.headers)

        if not response.ok:
            return {'status_code': response.status_code, 'text': response.text, 'ok': False}

        if not response.status_code == 200:
            return {'status_code': response.status_code, 'text': response.text, 'ok': True}

        return {'status_code': response.status_code, 'data': response.json(), 'ok': True}

    def delete(self, url):
        url = self.base_url + url

        response = requests.delete(url, auth=self.auth, headers=self.headers)

        if not response.ok:
            return {'status_code': response.status_code, 'text': response.text, 'ok': False}

        if not response.status_code == 204:
            return {'status_code': response.status_code, 'text': response.text, 'ok': False}

        return {'status_code': response.status_code, 'text': response.text, 'ok': True}
