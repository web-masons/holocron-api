[![Build Status](https://travis-ci.org/web-masons/holocron-api.svg)](https://travis-ci.org/web-masons/holocron-api)
[![Coverage Status](https://coveralls.io/repos/web-masons/holocron-api/badge.svg)](https://coveralls.io/r/web-masons/holocron-api)
[![Code Climate](https://codeclimate.com/github/web-masons/holocron-api/badges/gpa.svg)](https://codeclimate.com/github/web-masons/holocron-api)
# holocron-api
 
# Intro
 This is the API for the Holocron project.  It is built using Vagrant, Ansible, Python, Django and Django REST framework.
 
## To Install and run
 1. <p>Clone (or Fork) repository </p>
 2. <p>cd to /holocron_api folder, where Vagrantile is located </p>
 <p>      -Note: A local postgres db will be created using settings as configured in ansible/localhost/db/tasks/main.yml.  
   If you would like to use an alternate local db config, please modify the django local project settings located in 
   holocron_api/holocron_api/settings/local.py</p>
 3. <p><code> vagrant up </code> </p>
 4. <p> SSH into your vagrant environment and go to your django folder where manage.py exists the default is /vagrant/holocron_api. 
 Setup the database by running <code>python manage.py migrate</code>
 </p>
 5. <p> View test API at https://holocron-api.com/ </p>
 6. <p><i> Note: /placement-details/ does not display correctly at root.  This is a Django rest bug.  The url itself does still work. </i></p>

## To Run tests
    python manage.py test
- Run from main app folder in vagrant box where <i>manage.py</i> is present.
- This will run both the unit tests as well as the PEP 8 tests.


#### To run tests for a single app
    python manage.py test *app_name*
    
- Can be run on: 'api', 'pep8' and 'blacklist_manager'
 
## Deployment
 <p>Hashicorp's Atlas can be used to build and deploy. If you will be using Atlas, don't forget to add your atlas application to your push config in the Vagrantfile.</p>
 <p>This project includes 3 ansible roles.  The Base and Django roles will setup the base environment for running in stage or prod.  
 The Db role can be run in dev to create a local db.  These roles will configure an apache server with mod_wsgi to server the app. 
 If you don't want to use ansible, you can setup any wsgi server to serve the /holocron_api/holocron_api/wsgi.py application.
 </p>
 <p>To run in multiple environments, set the following env vars.  In apache with mod_sgi, this can be done by setting the vars for apache 
 with /etc/apache2/envvars then setting the virtualhost to pass these vars into the vhost.  The wsgi.py will pick them up from there and 
 provide to the app.</p>
 
### Included Apps (Endpoints)
- API: Manages links and link generation of marketing placements
- Blacklist Manager: Creates a Blacklist database to use for filtering in other Applications
 
 
### DJANGO_SETTINGS_MODULE 
<p>Name of the settings file for your env. Located in holocron_api/settings.  We pickup from settings.local if not defined. We have included
 prod, stage, and travis config examples.  These each inherit from base.py</p>

### DJANGO_SECRET_KEY
<p>This is a secret. Will be picked up by travis, stage, and prod configs.  Otherwise we use the preset key in local.py.  Please change
 this in production as many of django's security features use this and expect it to be secret.</p>

### HOLOCRON_ENV
<p>This is environment you are in.  Currently unused.</p>

### HOLOCRON_DB_USER
<p>The user for the database. Will be picked up by travis, stage, and prod configs.  Otherwise we use the preset value in local.py.</p>

### HOLOCRON_DB_PASS
<p>The password for the database. Will be picked up by travis, stage, and prod configs.  Otherwise we use the preset value in local.py.</p>

### HOLOCRON_DB_HOST
<p>The hostname of the database server. Will be picked up by travis, stage, and prod configs.  Otherwise we use the preset value in local.py.</p>

### HOLOCRON_DB_PORT
<p>The port for the database. Will be picked up by travis, stage, and prod configs.  Otherwise we use the preset value in local.py.</p>

### HOLOCRON_DB_NAME
<p>The db name for the database. Will be picked up by travis, stage, and prod configs.  Otherwise we use the preset value in local.py.</p>

 
---
 
# Standard Models and fields for PCT API
## Source
 
    source_key = Slug (Max Length = 100 characters, PK)
    source_name = String (Max Length = 100)
    created_on = Date and Time
    updated = Date and Time
    
## Medium

    medium_key = Slug (Max Length = 100 characters, PK)
    medium_name = String (Max Length = 100)
    created_on = Date and Time
    updated = Date and Time

## Creative
 
    creative_id = Auto Incrementing ID (PK)
    creative_name = String (Max Length = 100)
    creative_description = String (Max Length = 140)
    created_on = Date and Time
    updated = Date and Time
    
## Program

    program_key = String (Max Length = 100 characters, PK)
    program_name = String (Max Length = 100)
    program_description = String (Max Length = 140)
    created_by = String (Max Length = 100)
    program_notes = String (Max Length = 140, optional)
    start_date = Date
    end_date = Date
    created_on = Date and Time
    updated = Date and Time
    
## Campaign

    campaign_key = String (Max Length = 100 characters, PK)
    campaign_name = String (Max Length = 100)
    campaign_description = String (Max Length = 140)
    created_by = String (Max Length = 100)
    campaign_notes = String (Max Length = 140, optional)
    program = Program FK
    start_date = Date
    end_date = Date
    created_on = Date and Time
    updated = Date and Time

## Tactic

    tactic_id = Auto Incrementing ID (PK)
    tactic_key = Slug (Max Length = 100 characters)
    tactic_name = String (Max Length = 100)
    tactic_description = String (Max Length = 140)
    created_by = String (Max Length = 100)
    tactic_notes = String (Max Length = 140, optional)
    campaign = Campaign FK
    start_date = Date
    end_date = Date
    created_on = Date and Time
    updated = Date and Time

## Placement

    placement_id = Auto Incrementing ID (PK)
    placement_name = String (Max Length = 100)
    placement_url = String (Max Length = 100)
    tactic = Tactic FK
    medium = Medium FK
    source = Source FK
    creative = Creative FK
    catid = Integer (optional)
    jira_ticket = String (Max Length = 20, optional)
    pageID = String (optional)
    pageCat = String (optional)
    ad_network = Ad_Network FK (optional)
    start_date = Date
    end_date = Date
    created_on = Date and Time
    updated = Date and Time
    
# Custom Attributes Models and Fields# 
## Intent
 
    intent_key = Slug (PK)
    intent_description = String (Max Length = 140)
    created_on = Date and Time
    updated = Date and Time
    
## Audience
 
    audience_key = Slug (PK)
    audience_description = String (Max Length = 140)
    created_on = Date and Time
    updated = Date and Time
    
## Lifecycle
 
    lifecycle_key = Slug (PK)
    lifecycle_description = String (Max Length = 140)
    created_on = Date and Time
    updated = Date and Time
    
## LOB
 
    lob_key = Slug (PK)
    lob_description = String (Max Length = 140)
    created_on = Date and Time
    updated = Date and Time
    
## Ad_Network
    network_key = String (Max Length = 100)
    network_description = String (Max Length = 140)
    created_on = Date and Time
    updated = Date and Time
    
    
# Custom Attribute Xref Tables

## Intent_xref
 
    i_key = Intent FK (intent_key)
    p_key = Placement FK (placement_id)
    
## Audience_xref
 
    a_key = Audience FK (audience_key)
    p_key = Placement FK (placement_id)
    
## Lifecycle_xref
 
    lc_key = LifeCycle FK (lifecycle_key)
    p_key = Placement FK (placement_id)
    
## LOB_xref
 
    lob_key = LOB FK (lob_key)
    p_key = Placement FK (placement_id)
    
---
 
# Standard Models and fields for Blacklist Manager API


## BlacklistEntry
    entry_type = string (Limited to 2 characters.
                        IP = IP Address
                        IR = IP Range (CIDR)
                        UA = User Agent)
    entry = String (IP - Valid IPv4 or IPv6 address
                    IR - Valid IPv4 CIDR address
                    UA - String)
    description = String (max_length=100)
    added_by = String (max_length=100)
    created_on = Date and Time
    updated = Date and Time
    
    

## Entries
    entry_type = string (Limited to 2 characters.
                        IP = IP Address
                        UA = User Agent)
    entry = String (IP - Valid IPv4 or IPv6 address
                    UA - String)
    description = String (max_length=100)
    updated_by = String (max_length=100)
    related_to = String (list of BlacklistEntry PKs that contain this IP address)
    created_on = Date and Time
    updated = Date and Time