# Agile CRM

A Python interface for the [Agile CRM API](https://github.com/agilecrm/rest-api).

## Installation

    $ pip install agile-crm-python
    
## Usage

    In [1]: from agilecrm import AgileCRM

    In [2]: EMAIL = 'your_email'
       ...: API_KEY = 'agilecrm_api_key'
       ...: DOMAIN = 'your_domain'
       
    In [3]: agile_client = AgileCRM(DOMAIN, EMAIL, API_KEY)
    
    In [4]: print(agile_client.contact.fetch('5649050225344512'))
    {'data': {'klout_score': '', 'is_duplicate_existed': False, 'properties': [{'type': 'SYSTEM', 'value': 'Baqsssaasdf2', 'name': 'first_name'}, {'type': 'SYSTEM', 'value': 'SomeCompany', 'name': 'company'}, {'type': 'SYSTEM', 'value': '+998934979894', 'name': 'phone'}, {'type': 'CUSTOM', 'value': 'SuperSource', 'name': 'Captured Source'}, {'type': 'SYSTEM', 'value': 'jrahmonov2@gmail.com', 'name': 'email'}], 'star_value': 4, 'created_time': 1498828722, 'lead_status_id': 0, 'last_emailed': 0, 'owner': {'email': 'jahongir@superdispatch.com', 'calendar_url': 'https://jahongir.agilecrm.com/calendar/Jahongir_Rahmonov', 'phone': '', 'id': 4840599839309824, 'calendarURL': 'https://jahongir.agilecrm.com/calendar/Jahongir_Rahmonov', 'name': 'Jahongir Rahmonov', 'pic': 'https://d1gwclp1pmzk26.cloudfront.net/img/gravatar/48.png', 'domain': 'jahongir', 'schedule_id': 'Jahongir_Rahmonov'}, 'entity_type': 'contact_entity', 'lead_score': 34, 'lead_converted_time': 0, 'browserId': [], 'id': 5649050225344512, 'is_lead_converted': False, 'updated_time': 1498854662, 'tags': ['ios', 'awesome'], 'is_client_import': False, 'last_called': 0, 'trashed_time': 0, 'type': 'PERSON', 'source': 'api', 'lead_source_id': 0, 'unsubscribeStatus': [], 'restored_time': 0, 'contact_company_id': '5714163003293696', 'tagsWithTime': [{'entity_type': 'tag', 'availableCount': 0, 'createdTime': 1498829643106, 'tag': 'ios'}, {'entity_type': 'tag', 'availableCount': 0, 'createdTime': 1498830015686, 'tag': 'awesome'}], 'emailBounceStatus': [], 'last_contacted': 0, 'is_duplicate_verification_failed': False, 'viewed': {'viewed_time': 1500654861002, 'viewer_id': 4840599839309824}, 'formId': 0, 'campaignStatus': [], 'viewed_time': 0, 'last_campaign_emaild': 0}, 'text': None, 'ok': True, 'status_code': 200}       
      
## Documentation
       
### Table of contents

**[1 Contact](#1-contact)**
  * [1 To create a contact](#11-to-create-a-contact)
  * [2 To fetch contact data](#12-to-fetch-contact-data)
  * [3 To delete a contact](#13-to-delete-a-contact)
  * [4 To update a contact](#14-to-update-a-contact)
  * [5 Update lead score by ID](#15-update-lead-score-by-id)
  * [6 Update star value by ID](#16-update-star-value-by-id)
  * [7 Update tags value by ID](#17-update-tags-value-by-id)
  * [8 Delete tags value by ID](#18-delete-tags-value-by-id)
  * [9 Search contacts/companies](#19-search-contactscompanies)
  * [10 Adding tags to a contact based on email](#110-adding-tags-to-a-contact-based-on-email)
  * [11 Delete tags to a contact based on email](#111-delete-tags-to-a-contact-based-on-email)
  * [12 Add score to a contact using email ID](#112-add-score-to-a-contact-using-email-id)
  

**[2. Company](#2-company)**
  * [1 To create a company](#21-to-create-a-company)
  * [2 To update a company](#22-to-update-a-company)
  * [3 To get a company by company id](#23-to-get-a-company-by-company-id)
  * [4 To delete a company by company id](#24-to-delete-a-company-by-company-id)
 
**[3. Deal (Opportunity)](#3-deal)**
  * [1 To create a deal](#31-to-create-a-deal)
  * [2 To update a deal](#32-to-update-a-deal)
  * [3 Create deal to a contact using email ID](#33-create-deal-to-a-contact-using-email-id)
  * [4 Get list of deal](#34-get-list-of-deal)
  * [5 Get deal by ID](#35-get-deal-by-id)
  * [6 Delete deal by ID](#36-delete-deal-by-id)

**[4. Note ](#4-note)**
  * [1 Create a note and relate that to contacts](#41-create-a-note-and-relate-that-to-contacts)
  * [2 Add note to a contact using email ID](#42-add-note-to-a-contact-using-email-id)
  * [3 Gets notes related to specific contact](#43-gets-notes-related-to-specific-contact)
  * [4 Delete a specific note from specific contact](#44-delete-a-specific-note-from-specific-contact)
  * [5 Create note to a deal](#45-create-note-to-a-deal)
  * [6 Update note to a deal](#46-update-note-to-a-deal)
  * [7 Gets notes related to specific deal](#47-gets-notes-related-to-specific-deal)
  
     
    All the following examples assume that you have agile_client configured as shown above
         
#### 1. Contact

#####  1.1 Create a contact

    contact_data = {
        "star_value": "4",
        "lead_score": "92",
        "tags": [
            "Lead",
            "Likely Buyer"
        ],
        "properties": [
            {
                "type": "SYSTEM",
                "name": "first_name",
                "value": "Los "
            },
            {
                "type": "SYSTEM",
                "name": "last_name",
                "value": "Bruikheilmer"
            },
            {
                "type": "SYSTEM",
                "name": "company",
                "value": "steady.inc"
            },
            {
                "type": "SYSTEM",
                "name": "email",
                "subtype": "work",
                "value": "akrambakram@yabba.com"
            },
            {
                "type": "CUSTOM",
                "name": "My Custom Field",
                "value": "Custom value"
            }
        ]
    }
    
    response = agile_client.contact.create(contact_data)
    
#####  1.2 Fetch a contact by id

    response = agile_client.contact.fetch('5649050225344512')
    
#####  1.3 Delete a contact by id

    response = agile_client.contact.delete('5649050225344512')
    
#####  1.4 Update a contact by id

    new_contact_data = {
        "properties": [
            {
                "type": "SYSTEM",
                "name": "last_name",
                "value": "Chan"
            },
            {
                "type": "CUSTOM",
                "name": "My Custom Field",
                "value": "Custom value change"
            }
        ]
    }
    
    response = agile_client.contact.update('5689413791121408', new_contact_data)
    
#####  1.5 Set a lead score for a contact

    response = agile_client.contact.set_lead_score(contact_id='5689413791121408', lead_score=100)
    
#####  1.6 Set a star value for a contact

    response = agile_client.contact.set_star_value(contact_id='5689413791121408', star_value=3)

#####  1.7 Add a tag to a contact

    response = agile_client.contact.set_tags(contact_id='5689413791121408', tags=['new_tag'])
    
#####  1.8 Remove a tag from a contact

    response = agile_client.contact.remove_tags(contact_id='5689413791121408', tags_to_remove=['new_tag'])
    
#####  1.9 Search for a contact
    
    response = agile_client.contact.find(q='los', page_size=15)
    
#####  1.10 Add a note to a contact

    response = agile_client.contact.add_notes(contact_id='5689413791121408', subject='Note Subject', description='Some Note')
    
#####  1.11 Get notes of a contact

    response = agile_client.contact.get_notes(contact_id='5689413791121408')
    
#####  1.12 Delete a note of a contact    
    
    respose = agile_client.contact.delete_note(contact_id='5689413791121408', note_id='5755685136498688')

