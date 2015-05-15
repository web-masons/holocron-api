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
 
 