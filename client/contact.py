

class Contact:
    def __init__(self, requester):
        self.requester = requester

    def fetch(self, contact_id):
        url = 'contacts/{id}'.format(id=contact_id)

        return self.requester.get(url)
