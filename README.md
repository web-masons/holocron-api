# holocron-api
 
 
 # Intro
 This is the API for the Holocron project.  It is built using Vagrant, Ansible, Python, Django and Django REST framework.
 
 # To Install and run
 1. Clone (or Fork) repository 
 2. cd to /holocron_api folder, where Vagrantile is located
 3.<p> <code> vagrant up </code> </p>
 4. <p> <code> vagrant ssh </code> into the vagrant box that is created </p>
 5. <p> <code> python manage.py runserver 192.168.42.42:80" </code> </p>
 6. View test API at https://holocron-api.com/
    
<i>(In progress...)</i>

 # To Run tests
 <p> <code> python manage.py test api </code> </p>