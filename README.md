
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
