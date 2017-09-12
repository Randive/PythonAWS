#This script is used to terminate the ec2 instance whose id we given in the script.

import boto
from boto import ec2

connection = ec2.connect_to_region('us-east-1')

connection.terminate_instances(instance_ids=['i-082bae32256b48e5f'])

