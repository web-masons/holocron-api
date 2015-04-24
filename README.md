# holocron-api
 
 
 # Intro
 This is the API for the Holocron project.  It is built using Vagrant, Ansible, Python, Django and Django REST framework.
 
 # To Install and run
 1. Clone (or Fork) repository 
 2. cd to /holocron_api
 3. vagrant up
 4. ssh into the vagrant box that is created
 5. run "python manage.py runserver 192.168.42.42:80"
 6. View test API, navigate to the url from your Hostmanger entry
    - Either 192.168.42.42 OR holocron-api.vagrant.com
    - Hello World! API should be present
    
<i>(In progress...)</i>

 # To Run tests
 <code> python manage.py test api </code>