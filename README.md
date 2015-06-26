[![Build Status](https://travis-ci.org/web-masons/holocron-api.svg)](https://travis-ci.org/web-masons/holocron-api)
[![Coverage Status](https://coveralls.io/repos/web-masons/holocron-api/badge.svg)](https://coveralls.io/r/web-masons/holocron-api)
[![Code Climate](https://codeclimate.com/github/web-masons/holocron-api/badges/gpa.svg)](https://codeclimate.com/github/web-masons/holocron-api)
# holocron-api
 
 <h1>Intro </h1>
 This is the API for the Holocron project.  It is built using Vagrant, Ansible, Python, Django and Django REST framework.
 
 <h2>To Install and run </h2>
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

 <h2>To Run tests</h2>
 <p> <code> python manage.py test  </code>  - Run from main app folder in vagrant box where <i>manage.py</i> is present.
 - This will run both the unit tests as well as the PEP 8 tests.</p>
 
 <h2>Deployment</h2>

 <p>Hashicorp's Atlas can be used to build and deploy. If you will be using Atlas, don't forget to add your atlas application to your push config in the Vagrantfile.</p>

 <p>This project includes 3 ansible roles.  The Base and Django roles will setup the base environment for running in stage or prod.  
 The Db role can be run in dev to create a local db.  These roles will configure an apache server with mod_wsgi to server the app. 
 If you don't want to use ansible, you can setup any wsgi server to serve the /holocron_api/holocron_api/wsgi.py application.
 </p>
 
 <p>To run in multiple environments, set the following env vars.  In apache with mod_sgi, this can be done by setting the vars for apache 
 with /etc/apache2/envvars then setting the virtualhost to pass these vars into the vhost.  The wsgi.py will pick them up from there and 
 provide to the app.</p>
<h3>DJANGO_SETTINGS_MODULE<h3> 
<p>Name of the settings file for your env. Located in holocron_api/settings.  We pickup from settings.local if not defined. We have included
 prod, stage, and travis config examples.  These each inherit from base.py</p>

<h3>DJANGO_SECRET_KEY</h3>
<p>This is a secret. Will be picked up by travis, stage, and prod configs.  Otherwise we use the preset key in local.py.  Please change
 this in production as many of django's security features use this and expect it to be secret.</p>

<h3>HOLOCRON_ENV</h3>
<p>This is environment you are in.  Currently unused.</p>

<h3>HOLOCRON_DB_USER</h3>
<p>The user for the database. Will be picked up by travis, stage, and prod configs.  Otherwise we use the preset value in local.py.</p>

<h3>HOLOCRON_DB_PASS</h3>
<p>The password for the database. Will be picked up by travis, stage, and prod configs.  Otherwise we use the preset value in local.py.</p>

<h3>HOLOCRON_DB_HOST</h3>
<p>The hostname of the database server. Will be picked up by travis, stage, and prod configs.  Otherwise we use the preset value in local.py.</p>

<h3>HOLOCRON_DB_PORT</h3>
<p>The port for the database. Will be picked up by travis, stage, and prod configs.  Otherwise we use the preset value in local.py.</p>

<h3>HOLOCRON_DB_NAME</h3>
<p>The db name for the database. Will be picked up by travis, stage, and prod configs.  Otherwise we use the preset value in local.py.</p>

 
