from client import AgileCRM

EMAIL = 'vin@mysuperdispatch.com'
API_KEY = 'sbll51m5k7rrv1iig9eu4t23ll'
DOMAIN = 'superdispatch'


client = AgileCRM(DOMAIN, EMAIL, API_KEY)

print(client.contact.fetch("5103757536788480"))
