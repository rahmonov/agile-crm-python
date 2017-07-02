

class Deal:
    def __init__(self, requester):
        self.requester = requester

    def create(self, deal_data):
        url = 'opportunity'

        return self.requester.post(url, deal_data)

    def update(self, deal_id, deal_data):
        url = 'opportunity/partial-update'

        deal_data['id'] = deal_id

        return self.requester.put(url, deal_data)

    def fetch(self, deal_id):
        url = 'opportunity/{deal_id}'.format(deal_id=deal_id)

        return self.requester.get(url)

    def delete(self, deal_id):
        url = 'opportunity/{deal_id}'.format(deal_id=deal_id)

        return self.requester.delete(url)

    def add_notes(self, deal_id, subject, description):
        url = 'notes'

        data = {
            'subject': subject,
            'description': description,
            'deal_ids': [deal_id]
        }

        return self.requester.post(url, data)
