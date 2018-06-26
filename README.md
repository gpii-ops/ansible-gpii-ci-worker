Ansible role: gpii-ci-worker
===========================

Minimal Ansible role to manage CentOS 7.3 worker nodes running CI/CD for the [GPII](https://github.com/GPII). This includes:

  * [gitlab-runner](https://docs.gitlab.com/runner/) via [ansible-gitlab-runner](https://github.com/DBLaci/ansible-gitlab-runner)
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
 * [ansible-gitlab-runner](https://github.com/DBLaci/ansible-gitlab-runner)

Role Variables
--------------

```
# Docker Registry credentials are only active in production. Define these in
# vault.yml.
# gpii_ci_worker_docker_username: alice
# gpii_ci_worker_docker_password: secret
# gpii_ci_worker_docker_email: alice@example.com

# Passed to ansible-gitlab-runner
gpii_ci_worker_gitlab_runner_concurrent: 8

# Passed to ansible-gitlab-runner
gpii_ci_worker_gitlab_runner_registration_token: ""

# Passed to ansible-gitlab-runner
gpii_ci_worker_gitlab_runner_list: []

gpii_ci_worker_terraform_version: 0.11.7
# From e.g. https://releases.hashicorp.com/terraform/{{ gpii_ci_worker_terraform_version }}/terraform_{{ gpii_ci_worker_terraform_version }}_SHA256SUMS
gpii_ci_worker_terraform_checksum: sha256:6b8ce67647a59b2a3f70199c304abca0ddec0e49fd060944c26f666298e23418

gpii_ci_worker_terragrunt_version: 0.14.0

gpii_ci_worker_kubectl_version: v1.9.8

gpii_ci_worker_kops_version: 1.8.1
# From e.g. https://github.com/kubernetes/kops/releases/download/{{ gpii_ci_worker_kops_version }}/kops-darwin-amd64-sha1
gpii_ci_worker_kops_checksum: sha1:3f806f914d8bf2a0b9b3c6785689257b7aadcd17

gpii_ci_worker_helm_version: v2.8.2

gpii_ci_worker_aws_version: 1.15.45

gpii_ci_worker_jq_version: 1.5

gpii_ci_worker_ruby_version: 2.4.3

gpii_ci_worker_bundler_version: 1.16.1

gpii_ci_worker_rake_version: 12.3.0
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
