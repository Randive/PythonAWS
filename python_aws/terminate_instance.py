import boto
from boto import ec2

connection = ec2.connect_to_region('us-west-2')

connection.terminate_instances(instance_ids=['i-03d114d7bec489d8d'])
