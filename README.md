# Ansible Role: Clipbucket

[![Build Status](https://travis-ci.org/mtlynch/ansible-role-clipbucket.svg?branch=master)](https://travis-ci.org/mtlynch/ansible-role-clipbucket)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-clipbucket-blue.svg?style=flat-square)](https://galaxy.ansible.com/mtlynch/clipbucket)
[![License](http://img.shields.io/:license-apache-blue.svg?style=flat-square)](LICENSE)


Installs Clipbucket on Ubuntu 14.04 servers.

## Role Variables

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

## Dependencies

* geerlingguy.apache
* geerlingguy.php
* pcextreme.mariadb

## Example Playbook

##### `example.yml`

```yaml
- hosts: clipbucket
  roles:
    - { role: clipbucket }
```
### Running Example Playbook

To run the example playbook, `example.yml` run the commands below:

```bash
ansible-galaxy install mtlynch.clipbucket
ansible-playbook example.yml \
  --extra-vars "mysql_root_password=root" \
  --extra-vars "mysql_clipbucket_password=secret_db_password" \
  --extra-vars "clipbucket_admin_password=admin"
```

After executing the command above on a node called `clipbucket`, you would then navigate to http://clipbucket/ and log in using the credentials `admin` / `admin`.

In a playbook for a production server, you should create a `secrets.yml` file instead of specifying passwords on the command line and you should choose strong passwords instead of the examples.

## License

Apache2

## Author Information

This role was created in 2016 by [Michael Lynch](http://mtlynch.io).
