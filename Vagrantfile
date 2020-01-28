# -*- mode: ruby -*-
# vi: set ft=ruby :

#задаём количество машин
$node = 6

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.box_check_update = false
  
   (1..$node).each do |i|
        config.vm.define "node#{i}" do |node|
         node.vm.network  "public_network", ip: "192.168.1.#{110+i}"
         node.vm.hostname = "node#{i}"
         node.vm.provider "virtualbox" do |vb|
                vb.memory = "2048"
				vb.name = "node#{i}"
         end
        end
   end
   
   config.vm.provision "shell", inline: <<-SHELL
     sudo useradd -r minio-user -s /sbin/nologin
     sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config
     echo "vagrant:vagrant" | chpasswd
     systemctl restart sshd.service
     sudo apt -y install python
   SHELL
   #config.vm.provision "ansible" do |ansible|
    #ansible.playbook = "playbook.yml"
   #end
end

 

