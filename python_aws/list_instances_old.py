import boto
from boto import ec2

connection = ec2.connect_to_region('us-west-2')

reservations=connection.get_all_instances();
print "Instance Name \t \t \t IP Address\t\t Instance State\n"
for reservation in reservations:
 for instances in reservation.instances:
	 print "%s \t \t \t %s\t\t\t %s" % (instances.tags['Name'], instances.ip_address,instances.state) 
print "\n"
