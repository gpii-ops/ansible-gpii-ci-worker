import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_gitlab_service_enabled_and_running(Service):
    svc = Service("gitlab-runner")
    assert svc.is_enabled
    assert svc.is_running
