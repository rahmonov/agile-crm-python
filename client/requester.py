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
            error = 'HTTPError: {}, Details: {}'.format(response.status_code, response.text)

            return {'ok': False, 'error': error}

        return response.json()
