# Ansible Role: Clipbucket

[![Build Status](https://travis-ci.org/mtlynch/ansible-role-clipbucket.svg?branch=master)](https://travis-ci.org/mtlynch/ansible-role-clipbucket)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-clipbucket-blue.svg?style=flat-square)](https://galaxy.ansible.com/mtlynch/clipbucket)
[![License](http://img.shields.io/:license-apache-blue.svg?style=flat-square)](LICENSE)


Installs Clipbucket on Ubuntu 14.04 servers.

## Role Variables

Available variables are listed below, along with default values (see [defaults/main.yml](defaults/main.yml)):

```yaml
clipbucket_site_domain: example.com
```

```yaml
clipbucket_git_version: 4470
```

```yaml
clipbucket_path: /var/www/clipbucket
```

```yaml
clipbucket_mysql_db: clipbucketdb
clipbucket_mysql_user: clipbucketuser
clipbucket_mysql_prefix: cb_
```

```yaml
clipbucket_admin_user: admin
clipbucket_admin_password: 
```


## Dependencies

* [geerlingguy.apache](https://galaxy.ansible.com/geerlingguy/apache/)
* [geerlingguy.php](https://galaxy.ansible.com/geerlingguy/php/)
* [pcextreme.mariadb](https://galaxy.ansible.com/detail#/role/2462)

## Example Playbook

##### `example.yml`

```yaml
- hosts: clipbucket
  roles:
    - { role: clipbucket }
```
### Running Example Playbook

To run the example playbook, `example.yml` (above) run the commands below:

```bash
ansible-galaxy install mtlynch.clipbucket
ansible-playbook example.yml \
  --extra-vars "mysql_root_password=root" \
  --extra-vars "mysql_clipbucket_password=secret_db_password" \
  --extra-vars "clipbucket_admin_password=admin"
```

After executing the command above on a node called `clipbucket`, you would then navigate to [http://clipbucket/](http://clipbucket/) and log in using the credentials `admin` / `admin`.

In a playbook for a production server, you should create a `secrets.yml` file instead of specifying passwords on the command line and you should choose strong passwords instead of the examples.

## License

Apache2

## Author Information

This role was created in 2016 by [Michael Lynch](http://mtlynch.io).
