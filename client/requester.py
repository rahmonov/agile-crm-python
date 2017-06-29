import requests


class Requester:
    def __init__(self, domain, email, api_key):
        self.base_url = "https://{domain}.agilecrm.com/dev/api/".format(domain=domain)
        self.auth = (email, api_key)

    def get(self, url, content_type="application/json"):
        url = self.base_url + url
        headers = {
            'Accept': 'application/json',
            'content-type': content_type,
        }

        response = requests.get(url, auth=self.auth, headers=headers)

        if not response.ok:
            return {'status_code': response.status_code, 'text': response.text, 'ok': False}

        if not response.status_code == 200:
            return {'status_code': response.status_code, 'text': response.text, 'ok': True}

        return response.json()
