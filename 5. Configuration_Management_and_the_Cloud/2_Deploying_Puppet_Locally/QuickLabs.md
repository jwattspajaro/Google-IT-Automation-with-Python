### Puppet deployment
Install packages
#### There's a module named packages on the Puppet VM instance that takes care of installing the packages that are needed on the machines in the fleet. Use the command to visit the module:

**cd /etc/puppet/code/environments/production/modules/packages**


#### This module already has a resource entry specifying that python-requests is installed on all machines. You can see the init.pp file using the cat command on the Puppet VM instance.

**cat manifests/init.pp**
