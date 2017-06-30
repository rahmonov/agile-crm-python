

class Note:
    def __init__(self, requester):
        self.requester = requester

    def add_to_contacts(self, subject, description, contact_ids):
        url = 'notes'

        data = {
            'subject': subject,
            'description': description,
            'contact_ids': contact_ids
        }

        return self.requester.post(url, data)
