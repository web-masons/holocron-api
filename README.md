[![Build Status](https://travis-ci.org/web-masons/holocron-api.svg)](https://travis-ci.org/web-masons/holocron-api)
[![Coverage Status](https://coveralls.io/repos/web-masons/holocron-api/badge.svg)](https://coveralls.io/r/web-masons/holocron-api)
[![Code Climate](https://codeclimate.com/github/web-masons/holocron-api/badges/gpa.svg)](https://codeclimate.com/github/web-masons/holocron-api)
# holocron-api
 
 
 <h1>Intro </h1>
 This is the API for the Holocron project.  It is built using Vagrant, Ansible, Python, Django and Django REST framework.
 
 <h2>To Install and run </h2>
 1. <p>Clone (or Fork) repository </p>
 2. <p>cd to /holocron_api folder, where Vagrantile is located </p>
 <p>      -Note: If not already created, create "settings.ini" file inside of /ansible/localhost.  A template is provided.
 3. <p><code> vagrant up </code> </p>
 4. <p> SSH into your vagrant environment and go to your django folder where manage.py exists. 
 Setup the database by running <code>python manage.py makemigrations</code>
 followed by <code>python manage.py migrate</code> </p>
 5. <p> View test API at https://holocron-api.com/ </p>
 6. <p><i> Note: /placement-details/ does not display correctly at root.  This is a Django rest bug.  The url itself does still work. </i></p>
    
<i>(In progress...)</i>

 <h2>To Run tests</h2>
 <p> <code> python manage.py test  </code>  - Run from main app folder in vagrant box where <i>manage.py</i> is present.
 - This will run both the unit tests as well as the PEP 8 tests.</p>
 
---
 
<h1>Standard Models and fields</h1>
 <h2>Source</h2>
 
    source_key = Slug (Max Length = 100 characters, PK)
    source_name = String (Max Length = 100)
    created_on = Date and Time
    updated = Date and Time
    
 <h2>Medium</h2>

    medium_key = Slug (Max Length = 100 characters, PK)
    medium_name = String (Max Length = 100)
    created_on = Date and Time
    updated = Date and Time

 <h2>Creative</h2>
 
    creative_id = Auto Incrementing ID (PK)
    creative_name = String (Max Length = 100)
    creative_description = String (Max Length = 140)
    created_on = Date and Time
    updated = Date and Time

 <h2>Campaign</h2>

    campaign_key = Slug (Max Length = 100 characters, PK)
    campaign_name = String (Max Length = 100)
    campaign_description = String (Max Length = 140)
    created_by = String (Max Length = 100)
    campaign_notes = String (Max Length = 140, optional)
    end_date = Date
    created_on = Date and Time
    updated = Date and Time

 <h2>Placement</h2>

    placement_id = Auto Incrementing ID (PK)
    placement_name = String (Max Length = 100)
    placement_url = String (Max Length = 100)
    campaign = Campaign FK
    medium = Medium FK
    source = Source FK
    creative = Creative FK
    catid = Integer (optional)
    jira_ticket = String (Max Length = 20, optional)
    end_date = Date
    created_on = Date and Time
    updated = Date and Time
    
<h1>Custom Attributes Models and Fields<h1>
 <h2>Intent</h2>
 
    intent_key = Slug (PK)
    intent_description = String (Max Length = 140)
    created_on = Date and Time
    updated = Date and Time
    
 <h2>Audience</h2>
 
    audience_key = Slug (PK)
    audience_description = String (Max Length = 140)
    created_on = Date and Time
    updated = Date and Time
    
 <h2>Lifecycle</h2>
 
    lifecycle_key = Slug (PK)
    lifecycle_description = String (Max Length = 140)
    created_on = Date and Time
    updated = Date and Time
    
 <h2>LOB</h2>
 
    lob_key = Slug (PK)
    lob_description = String (Max Length = 140)
    created_on = Date and Time
    updated = Date and Time
    
    
<h1>Custom Attribute Xref Tables</h1>
  <h2>Intent_xref</h2>
 
    i_key = Intent FK (intent_key)
    p_key = Placement FK (placement_id)
    
 <h2>Audience_xref</h2>
 
    a_key = Audience FK (audience_key)
    p_key = Placement FK (placement_id)
    
 <h2>Lifecycle_xref</h2>
 
    lc_key = LifeCycle FK (lifecycle_key)
    p_key = Placement FK (placement_id)
    
 <h2>LOB_xref</h2>
 
    lob_key = LOB FK (lob_key)
    p_key = Placement FK (placement_id)
