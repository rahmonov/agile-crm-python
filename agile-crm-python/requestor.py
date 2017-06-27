import requests


class Requestor:
    def __init__(self, domain, email, api_key, content_type="application/json"):
        self.base_url = "https://{domain}.agilecrm.com/dev/api/".format(domain=domain)
        self.auth = (email, api_key)
        self.headers = {
            'Accept': 'application/json',
            'content-type': content_type,
        }

    def get(self, url):
        url = self.base_url + url

        response = requests.get(url, headers=self.headers, auth=self.auth)

        if not response.ok:
            error = 'HTTPError: {}, Details: {}'.format(response.status_code, response.text)

            return {'ok': False, 'error': error}

        return response.json()
