from .contact import Contact
from .requester import Requester


class AgileCRM:
    def __init__(self, domain, email, api_key):
        requester = Requester(domain, email, api_key)

        self.contact = Contact(requester=requester)
