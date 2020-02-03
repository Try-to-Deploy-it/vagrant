# vagrant

system configuration:
#VRRP

	priority	    120		    110		    100

	192.168.1.199	192.168.1.111	192.168.1.112	192.168.1.113
	192.168.1.198	192.168.1.112	192.168.1.113	192.168.1.111
	192.168.1.197	192.168.1.113	192.168.1.111	192.168.1.112

#Minio ports:
tenant_one: 80

    reverse proxy and balancing for:
   	192.168.1.111:9000
	192.168.1.112:9000
	192.168.1.113:9000
	192.168.1.114:9000
	192.168.1.115:9000
	192.168.1.116:9000
tenant_two: 81

	reverse proxy and balancing for:
	192.168.1.111:9001
	192.168.1.112:9001
	192.168.1.113:9001
	192.168.1.114:9001
	192.168.1.115:9001
	192.168.1.116:9001

#Autorization:

 node1-6:
 
	ssh_user: vagrant
	ssh_pass: vagrant
 
 minio system:
 
	access_key: minioadmin
	secret_key: minioadmin

#system startup commands
1. vagran up                      #to start VMs
2. ansible-playbook playbook.yml  #to configure services

3. ansible node1 -m shell -a "/vagrant/mc admin user add localhost:9000 newuser new_user123" # ad-hoc command to create new minio user

# the first way to upload file
4.1 ansible node1 -m shell -a "/vargant/mc cp /vagrant/test.jpg testbucket" 

# the second way to upload file
4.2 ansible node1 -m aws_s3 -a "bucket=testbucket object=test.jpg src=./test.jpg mode=put aws_access_key='minioadmin' aws_secret_key='minioadmin'"

# the third way to upload file
4.3 ansible node1 -m copy -a "src=./test.jpg dest=/vagrant/minio_two/testbucket"

# python script dowloading the file with offset
5. file.py 
