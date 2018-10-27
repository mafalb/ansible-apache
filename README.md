
# An ansible role for Apache httpd          [![Build Status](https://www.travis-ci.com/mafalb/ansible-apache.svg?branch=master)](https://www.travis-ci.com/mafalb/ansible-apache)

## Requirements

put the following into your **ansible.cfg**
the use of dictionaries inside the code demand this.

```
hash_behaviour = merge
```

if you want to install a httpd from a **software collection** then you obviously need the appropriate package repository enabled.

## Basic Usage

This will install the default Apache Webserver for your distribution

```
- hosts: localhost
  roles:
    - role: apache/daemon
```

## Variables

```
apache_scl_name: false
```
The name of the Software Collection to install

```
apache_scl_enabled: false
```
If the collection should be enabled. The equivalent on the command line would be something like `$ scl enable httpd24 bash` .  This will symlink the enable script from /opt/rh/httpd24/enable

```
apache_service_managed: true
```
Set this to false if apache is managed by cluster software like pacemaker or heartbeat, i.e. you don't want your default service manager to care about it.

## Examples

```
- hosts: localhost
  vars:
    apache_scl_name: httpd24
    apache_scl_enabled: true
  roles:
    - role: scl
    - role: apache/daemon
```

```
- hosts: localhost
  vars:
    apache_scl_name: httpd24
    apache_scl_enabled: true
    apache_scl_prefix: rh
  roles:
    - role: scl
    - role: apache/daemon
```


