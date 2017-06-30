

class Company:
    def __init__(self, requester):
        self.requester = requester

    def create(self, company_data):
        url = 'contacts'

        if 'type' not in company_data:
            company_data['type'] = 'COMPANY'

        return self.requester.post(url, company_data)

    def update(self, company_id, company_data):
        url = 'contacts/edit-properties'

        company_data['id'] = company_id

        return self.requester.put(url, company_data)

    def fetch(self, company_id):
        url = 'contacts/{id}'.format(id=company_id)

        return self.requester.get(url)

    def delete(self, company_id):
        url = 'contacts/{id}'.format(id=company_id)

        return self.requester.delete(url)
