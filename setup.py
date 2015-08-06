from setuptools import setup

setup(
    name='check_no_scheduled_ec2_events',
    version='0.2.0',
    packages=['check_no_scheduled_ec2_events', ],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    description='Nagios-style check if the current EC2 instance has any scheduled events',
    long_description=open('README.rst').read(),
    install_requires=open('requirements.txt').read(),
    author='Martin Melin',
    author_email='martin@tictail.com',
    url='http://github.com/martinmelin/check_no_scheduled_ec2_events',
    entry_points={
        'console_scripts': ['check_no_scheduled_ec2_events = check_no_scheduled_ec2_events:check'],
    }
)
