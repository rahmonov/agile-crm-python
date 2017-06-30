

class Contact:
    def __init__(self, requester):
        self.requester = requester

    def create(self, contact_data):
        url = 'contacts'

        return self.requester.post(url, contact_data)

    def fetch(self, contact_id):
        url = 'contacts/{id}'.format(id=contact_id)

        return self.requester.get(url)

    def update(self, contact_id, contact_data):
        url = 'contacts/edit-properties'

        contact_data['id'] = contact_id

        return self.requester.put(url, contact_data)

    def delete(self, contact_id):
        url = 'contacts/{id}'.format(id=contact_id)

        return self.requester.delete(url)
