VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # Get rid of that pesky "stdin: is not a tty" error
  config.ssh.shell = "bash -c 'BASH_ENV=/etc/profile exec bash'"

  # Use Ansible Citadel box
  #config.vm.box = "oakensoul/ansible-citadel"
  config.vm.box = "ubuntu/trusty64"

  # Forward SSH keys to the Guest VM
  config.ssh.forward_agent = true

  #Setup hostmanager config to update the host files
  config.hostmanager.enabled = true
  config.hostmanager.manage_host = true
  config.hostmanager.ignore_private_ip = false
  config.hostmanager.include_offline = true
  #config.vm.provision :hostmanager
  config.vm.define 'holocron-api' do |node|
      node.vm.hostname = 'holocron-api.com'
      node.vm.network :private_network, ip: '192.168.42.42'
  end

  #install ansible
    config.vm.provision :shell,
      :privileged => true,
      :keep_color => true,
      :inline => "apt-get -y install software-properties-common && apt-add-repository ppa:ansible/ansible && apt-get update && apt-get -y install ansible"


  # We're going to use the shell provider to install Ansible so that we can run
  # it within the Guest VM, not outside
  config.vm.provision :shell,
      :privileged => true,
      :keep_color => true,

      :inline => "export PYTHONUNBUFFERED=1 && export ANSIBLE_FORCE_COLOR=1 && cd /vagrant/ansible && ansible-galaxy install -r localhost/requirements.txt -p localhost/ --force && cd /vagrant/ansible/localhost && ./provision.sh"

  config.push.define "atlas" do |push|
    push.app = ""
    push.vcs = true
  end

end
