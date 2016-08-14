Ansible Role: Clipbucket
=========

[![Build Status](https://travis-ci.org/mtlynch/ansible-role-clipbucket.svg?branch=master)](https://travis-ci.org/mtlynch/ansible-role-clipbucket)


Installs Clipbucket on Ubuntu 14.04 servers.

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Dependencies
------------

* geerlingguy.apache
* geerlingguy.php
* pcextreme.mariadb

Example Playbook
----------------

```yaml
- hosts: clipbucket
  roles:
    - { role: clipbucket }
```

License
-------

Apache2

Author Information
------------------

This role was created in 2016 by [Michael Lynch](http://mtlynch.io).
