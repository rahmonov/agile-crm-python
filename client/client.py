from .company import Company
from .contact import Contact
from .deal import Deal
from .note import Note
from .requester import Requester


class AgileCRM:
    def __init__(self, domain, email, api_key):
        requester = Requester(domain, email, api_key)

        self.contact = Contact(requester=requester)
        self.company = Company(requester=requester)
        self.deal = Deal(requester=requester)
        self.note = Note(requester=requester)
