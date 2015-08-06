# -*- encoding: utf-8 -*-
"""A Nagios-style script that will check if the Amazon EC2 instance it is running
on has any events scheduled, like a system reboot.

Exit code 2 if any events are scheduled, 0 otherwise. Useful in combination
with Nagios and/or NRPE.

Usage:
    check_no_scheduled_ec2_events
    check_no_scheduled_ec2_events -h | --help

No options are given. The script assumes it is running in an EC2 instance, and
will grab the current instance id from the instance metadata and AWS
credentials from the current environment."""
import sys
import docopt
import boto.ec2
import boto.utils

def get_region_from_az(az):
    # Assumes we can just drop the last character of the AZ to get region name:
    return az[:-1]

def check():
    # No arguments yet, but let docopt handle --help:
    docopt.docopt(__doc__)

    # Grab current instance metadata (will hang if not in EC2)
    current_instance = boto.utils.get_instance_metadata()
    instance_id = current_instance['instance-id']
    current_az = current_instance['placement']['availability-zone']

    # Connect to EC2 API (assumes valid credentials in OS environment)
    connection = boto.ec2.connect_to_region(get_region_from_az(current_az))

    # Get instance status for the EC2 instance we are running on:
    instance_status = connection.get_all_instance_status(instance_ids=[instance_id]).pop()

    # Filter out schedueld events that already have been completed
    scheduled_events = filter(lambda e: '[Completed]' not in e.description, instance_status.events)
    if scheduled_events:
        print "CRITICAL: instance %s has scheduled events: %s" % (instance_id, scheduled_events)
        sys.exit(2)

    print "OK: instance %s has no scheduled events" % instance_id

if __name__ == "__main__":
    check()
