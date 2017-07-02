

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

    def add_to_deals(self, subject, description, deal_ids):
        url = 'opportunity/deals/notes'

        data = {
            'subject': subject,
            'description': description,
            'deal_ids': deal_ids
        }

        return self.requester.post(url, data)
