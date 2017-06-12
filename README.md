Ansible role: gpii-ci-worker
===========================

Minimal Ansible role to manage CentOS 7.3 worker nodes running CI/CD for the [GPII](https://github.com/GPII). This includes:

  * [gitlab-runner](https://docs.gitlab.com/runner/) via [ansible-gitlab-runner](https://github.com/mrtyler/ansible-gitlab-runner)
  * [Terraform](https://www.terraform.io/) and [Terragrunt](https://github.com/gruntwork-io/terragrunt)
  * [jq](https://stedolan.github.io/jq/)
  * [rvm](https://rvm.io/) and [bundler](http://bundler.io/)
  * git configuration for `gitlab-runner` user
  * ssh config (private key delivered out-of-band)

Requirements
------------

 * CentOS 7.x
 * Ansible 2.x
 * systemd
 * [ansible-gitlab-runner](https://github.com/mrtyler/ansible-gitlab-runner)

Role Variables
--------------

```
# Passed to ansible-gitlab-runner
gpii_ci_worker_gitlab_runner_registration_token: ""

# Passed to ansible-gitlab-runner
gpii_ci_worker_gitlab_runner_list: []

gpii_ci_worker_terraform_version: 0.9.5
# From e.g. https://releases.hashicorp.com/terraform/{{ gpii_ci_worker_terraform_version }}/terraform_{{ gpii_ci_worker_terraform_version }}_SHA256SUMS
gpii_ci_worker_terraform_checksum: sha256:0cbb5474c76d878fbc99e7705ce6117f4ea0838175c13b2663286a207e38d783

gpii_ci_worker_terragrunt_version: 0.12.6

gpii_ci_worker_jq_version: 1.5

gpii_ci_worker_ruby_version: 2.4.0
```

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
