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
  * [1 Create a contact](#11-create-a-contact)
  * [2 Fetch a contact by ID](#12-fetch-a-contact-by-id)
  * [3 Delete a contact by ID](#13-delete-a-contact-by-id)
  * [4 Update a contact by ID](#14-update-a-contact-by-id)
  * [5 Set a lead score for a contact](#15-set-a-lead-score-for-a-contact)
  * [6 Set a star value for a contact](#16-set-a-star-value-for-a-contact)
  * [7 Add a tag to a contact](#17-add-a-tag-to-a-contact)
  * [8 Remove a tag from a contact](#18-remove-a-tag-from-a-contact)
  * [9 Search for a contact](#19-search-for-a-contact)
  * [10 Add a note to a contact](#110-add-a-note-to-a-contact)
  * [11 Get notes of a contact](#111-get-notes-of-a-contact)
  * [12 Delete a note of a contact](#112-delete-a-note-of-a-contact)
  
**[2 Company](#2-company)**
  * [1 Create a company](#21-create-a-company)
  * [2 Fetch a company by ID](#22-fetch-a-company-by-id)
  * [3 Update a company by ID](#23-update-a-company-by-id)
  * [4 Delete a company by ID](#24-delete-a-company-by-id)
  
  
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



#### 2. Company

#####  2.1 Create a company

    company_data = {
        "type": "COMPANY",
        "star_value": 4,
        "lead_score": 120,
        "tags": [
            "Permanent",
            "USA",
        ],
        "properties": [
            {
                "name": "Company Type",
                "type": "CUSTOM",
                "value": "MNC Inc"
            },
            {
                "type": "SYSTEM",
                "name": "name",
                "value": "Spicejet"
            },
            {
                "type": "SYSTEM",
                "name": "url",
                "value": "http://www.spicejet.com/"
            },
            {
                "name": "email",
                "value": "care@spicejet.com  ",
                "subtype": ""
            },
            {
                "name": "phone",
                "value": "45500000",
                "subtype": ""
            },
            {
                "name": "website",
                "value": "http://www.linkedin.com/company/agile-crm",
                "subtype": "LINKEDIN"
            },
            {
                "name": "address",
                "value": "{\"address\":\"MS 35, 440 N Wolfe Road\",\"city\":\"Sunnyvale\",\"state\":\"CA\",\"zip\":\"94085\",\"country\":\"US\"}",
                "subtype": "office"
            }
        ]
    }
    
    response = agile_client.company.create(company_data)
    
#####  2.2 Fetch a company by id    
    
    respose = agile_client.company.fetch('5712536552865792')
    
#####  2.3 Update a company by id

    new_company_data = {
        "properties": [
            {
                "type": "SYSTEM",
                "name": "name",
                "value": "SPICE JET"
            },
            {
                "type": "SYSTEM",
                "name": "url",
                "value": "http://www.spicejet.com/"
            },
            {
                "name": "phone",
                "value": "45500000",
                "subtype": ""
            }
        ]
    }

    response = agile_client.company.update('5712536552865792', new_company_data)
    
#####  2.4 Delete a company by id

    response = agile_client.company.delete('5712536552865792')