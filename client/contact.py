

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

    def set_lead_score(self, contact_id, lead_score):
        url = 'contacts/edit/lead-score'

        data = {
            'id': contact_id,
            'lead_score': lead_score
        }

        return self.requester.put(url, data)

    def set_star_value(self, contact_id, star_value):
        url = 'contacts/edit/add-star'

        data = {
            'id': contact_id,
            'star_value': star_value
        }

        return self.requester.put(url, data)
