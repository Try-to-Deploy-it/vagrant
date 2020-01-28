# vagrant
1. vagran up                      #to start VMs
2. ansible-playbook playbook.yml  #to configure services

3. ansible node1 -m shell -a "/vagrant/mc admin user add localhost:9000 newuser new_user123" # ad-hoc command to create new minio user

4.1 ansible node1 -m shell -a "/vargant/mc cp /vagrant/test.jpg testbucket" 
# the first way to upload file.

4.2 ansible node1 -m aws_s3 -a "bucket=testbucket object=test.jpg src=./test.jpg mode=put aws_access_key='minioadmin' aws_secret_key='minioadmin'"
# the second way to upload file

4.3 ansible node1 -m copy -a "src=./test.jpg dest=/vagrant/minio_two/testbucket"
# the third way to upload file

5. file.py - python script dowloading the file with offset