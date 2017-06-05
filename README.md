Ansible role: gpii-ci-worker
===========================

Minimal Ansible role to manage CentOS 7.3 worker nodes to run CI/CD for the GPII. This includes:

  * tf/tg, rvm/rb/bundle, ...

Requirements
------------

 * CentOS 7.x
 * Ansible 2.x
 * systemd

Role Variables
--------------

Example Playbook
----------------

    - hosts: servers
      roles:
         - ansible-gpii-ci-worker

Tests
-----

Use [molecule](https://github.com/metacloud/molecule) to test this role.

Because this role depends on systemd and might one day need SELinux (as related role ansible-influxdb does), only a Vagrant provider is configured at the moment.

License
-------

MIT

Author Information
------------------

Raising the Floor - US
