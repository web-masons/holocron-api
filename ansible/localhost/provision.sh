#!/usr/bin/env bash

cd /vagrant/ansible
ansible-playbook localhost/vagrant.yml --inventory-file=inventory/vagrant.ini --connection=local
