
apache_scl_name: the name of the software collection
apache_scl_enabled: if the collection should be enabled
apache_service_managed: set to false if apache is managed by cluster software

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

```
- hosts: ess
  roles:
    - role: apache/daemon
```
