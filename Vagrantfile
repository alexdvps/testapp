# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.network "forwarded_port", guest: 3000, host: 3000

  config.vm.provision "docker" do |docker|
    docker.build_image "/vagrant", args: "-t vagrant/testapp"
    docker.run "vagrant/testapp" , args: "-p 3000:3000"
  end
end
