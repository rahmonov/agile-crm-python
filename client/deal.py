

class Deal:
    def __init__(self, requester):
        self.requester = requester

    def create(self, deal_data):
        url = 'opportunity'

        return self.requester.post(url, deal_data)
