import boto
from boto import ec2

connection = ec2.connect_to_region('us-west-2')

compute_resources=connection.get_all_instances();
print "\tInstance Name\t \t \t \t IP Address\t\t\t\t Instance State\n"
for resource in compute_resources:
 for instances in resource.instances:
	 print "%20s \t \t \t %15s \t\t\t %15s " % (instances.tags['Name'], instances.ip_address,instances.state) 
print "\n"
