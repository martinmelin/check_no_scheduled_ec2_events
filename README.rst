A Nagios-style script that will check if the Amazon EC2 instance it is running
on has any events scheduled, like a system reboot.

Exit code 2 if any events are scheduled, 0 otherwise. Useful in combination
with Nagios and/or NRPE.

Usage:
    check_no_scheduled_ec2_events

No options are given. The script assumes it is running in an EC2 instance, and
will grab the current instance id from the instance metadata and AWS
credentials from the current environment.

Changelog:

0.2.1 - Handle `events` being None in boto `InstanceStatus`

0.2.0 - Handle case where a "completed" scheduled event still shows up in API

0.1.1 - Initial public release
