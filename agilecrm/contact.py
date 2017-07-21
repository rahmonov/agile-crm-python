

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

    def set_tags(self, contact_id, tags):
        url = 'contacts/edit/tags'

        data = {
            'id': contact_id,
            'tags': tags
        }

        return self.requester.put(url, data)

    def remove_tags(self, contact_id, tags_to_remove):
        url = 'contacts/delete/tags'

        data = {
            'id': contact_id,
            'tags': tags_to_remove
        }

        return self.requester.put(url, data)

    def find(self, q, page_size=10):
        url = 'search'

        params = {
            'q': q,
            'page_size': page_size,
            'type': 'PERSON'
        }

        return self.requester.get(url, params)

    def add_notes(self, contact_id, subject, description):
        url = 'notes'

        data = {
            'subject': subject,
            'description': description,
            'contact_ids': [contact_id]
        }

        return self.requester.post(url, data)

    def get_notes(self, contact_id):
        url = 'contacts/{contact_id}/notes'.format(contact_id=contact_id)

        return self.requester.get(url)

    def delete_note(self, contact_id, note_id):
        url = 'contacts/{contact_id}/notes/{note_id}'.format(contact_id=contact_id, note_id=note_id)

        return self.requester.delete(url)
