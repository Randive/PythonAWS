import boto
from boto import ec2

connection = ec2.connect_to_region('us-west-2')

reservation=connection.run_instances(
    image_id='ami-d94f5aa0',
    key_name='test00',
    instance_type='t2.micro',
    security_groups=['test_group']
)

instance = reservation.instances[0]
print instance
print "\n"
connection.create_tags([instance.id],{"Name": 'instance_test'})

compute_resources=connection.get_all_instances();

print "\tInstance Name\t \t \t \t IP Address\t\t\t\t Instance State\n"

for resource in compute_resources:
 for instances in resource.instances:
         print "%20s \t \t \t %15s \t\t\t %15s " % (instances.tags['Name'], instances.ip_address,instances.state)
print "\n"


