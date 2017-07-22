## Agile CRM

A Python interface for the [Agile CRM API](https://github.com/agilecrm/rest-api).

### Installation

    $ pip install agile-crm-python
    
### Usage

    In [1]: from agilecrm import AgileCRM

    In [2]: EMAIL = 'your_email'
       ...: API_KEY = 'agilecrm_api_key'
       ...: DOMAIN = 'your_domain'
       
    In [3]: agile_client = AgileCRM(DOMAIN, EMAIL, API_KEY)
    
    In [4]: print(agile_client.contact.fetch('5649050225344512'))
    {'data': {'klout_score': '', 'is_duplicate_existed': False, 'properties': [{'type': 'SYSTEM', 'value': 'Baqsssaasdf2', 'name': 'first_name'}, {'type': 'SYSTEM', 'value': 'SomeCompany', 'name': 'company'}, {'type': 'SYSTEM', 'value': '+998934979894', 'name': 'phone'}, {'type': 'CUSTOM', 'value': 'SuperSource', 'name': 'Captured Source'}, {'type': 'SYSTEM', 'value': 'jrahmonov2@gmail.com', 'name': 'email'}], 'star_value': 4, 'created_time': 1498828722, 'lead_status_id': 0, 'last_emailed': 0, 'owner': {'email': 'jahongir@superdispatch.com', 'calendar_url': 'https://jahongir.agilecrm.com/calendar/Jahongir_Rahmonov', 'phone': '', 'id': 4840599839309824, 'calendarURL': 'https://jahongir.agilecrm.com/calendar/Jahongir_Rahmonov', 'name': 'Jahongir Rahmonov', 'pic': 'https://d1gwclp1pmzk26.cloudfront.net/img/gravatar/48.png', 'domain': 'jahongir', 'schedule_id': 'Jahongir_Rahmonov'}, 'entity_type': 'contact_entity', 'lead_score': 34, 'lead_converted_time': 0, 'browserId': [], 'id': 5649050225344512, 'is_lead_converted': False, 'updated_time': 1498854662, 'tags': ['ios', 'awesome'], 'is_client_import': False, 'last_called': 0, 'trashed_time': 0, 'type': 'PERSON', 'source': 'api', 'lead_source_id': 0, 'unsubscribeStatus': [], 'restored_time': 0, 'contact_company_id': '5714163003293696', 'tagsWithTime': [{'entity_type': 'tag', 'availableCount': 0, 'createdTime': 1498829643106, 'tag': 'ios'}, {'entity_type': 'tag', 'availableCount': 0, 'createdTime': 1498830015686, 'tag': 'awesome'}], 'emailBounceStatus': [], 'last_contacted': 0, 'is_duplicate_verification_failed': False, 'viewed': {'viewed_time': 1500654861002, 'viewer_id': 4840599839309824}, 'formId': 0, 'campaignStatus': [], 'viewed_time': 0, 'last_campaign_emaild': 0}, 'text': None, 'ok': True, 'status_code': 200}       
      
### Documentation
       
***coming soon***