

class Company:
    def __init__(self, requester):
        self.requester = requester

    def fetch(self, company_id):
        url = 'contacts/{id}'.format(id=company_id)

        return self.requester.get(url)
