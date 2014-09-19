# -*- encoding: utf-8 -*-
import sys
import boto.ec2
import boto.utils

def get_region_from_az(az):
    # Assumes we can just drop the last character of the AZ to get region name:
    return az[:-1]

def check():
    # Grab current instance metadata (will hang if not in EC2)
    current_instance = boto.utils.get_instance_metadata()
    instance_id = current_instance['instance-id']
    current_az = current_instance['placement']['availability-zone']

    # Connect to EC2 API (assumes valid credentials in OS environment)
    connection = boto.ec2.connect_to_region(get_region_from_az(current_az))

    # Get instance status for the EC2 instance we are running on:
    instance_status = connection.get_all_instance_status(instance_ids=[instance_id]).pop()

    if instance_status.events:
        print "CRITICAL: instance %s has scheduled events: %s" % (instance_id, instance_status.events)
        sys.exit(2)

    print "OK: instance %s has no scheduled events" % instance_id
