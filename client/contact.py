

class Contact:
    def __init__(self, requester):
        self.requester = requester

    def fetch(self, contact_id):
        url = 'contacts/{id}'.format(id=contact_id)

        # todo: return an object to be able to do this: contact = client.contact.fetch('123131') \n contact.get('name')
        # todo: this object can also return a json representation of its data: contact.json()
        return self.requester.get(url)
