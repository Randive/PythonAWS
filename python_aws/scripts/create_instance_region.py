# This script is used to create an instance in us-east-1 region and displaying all the instances in the same region.

import boto
from boto import ec2

connection = ec2.connect_to_region('us-east-1')

reservation=connection.run_instances(
    image_id='ami-4b133c5d',
    key_name='demoPuppet',
    instance_type='t2.micro',
    security_groups=['test_group']
)

instance = reservation.instances[0]
print instance
print "\n"
connection.create_tags([instance.id],{"Name": 'demo_instance'})

compute_resources=connection.get_all_instances();

print "\tInstance Name\t \t \t \t IP Address\t\t\t\t Instance State\n"

for resource in compute_resources:
 for instances in resource.instances:
         print "%20s \t \t \t %15s \t\t\t %15s " % (instances.tags['Name'], instances.ip_address,instances.state)
print "\n"


