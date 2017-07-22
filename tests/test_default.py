import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_gitlab_service_enabled_and_running(Service):
    svc = Service("gitlab-runner")
    assert svc.is_enabled
    assert svc.is_running


def test_terraform_installed(Command):
    assert Command.exists("terraform")


def test_terragrunt_installed(Command):
    assert Command.exists("terragrunt")


def test_kubectl_installed(Command):
    assert Command.exists("kubectl")


def test_jq_installed(Command):
    assert Command.exists("jq")


def test_rvm_gpg_key_imported(Command, Sudo):
    with Sudo("gitlab-runner"):
        gpg_list_keys = Command.check_output("gpg --list-keys")
    assert "Michal Papis (RVM signing) <mpapis@gmail.com>" in gpg_list_keys


def test_rvm_installed_only_for_gitlab_runner(Command, File, Sudo):
    assert not Command.exists("rvm")
    with Sudo("gitlab-runner"):
        assert File("/home/gitlab-runner/.rvm/bin/rvm").exists


def test_ruby_installed_with_rvm(File, Sudo):
    with Sudo("gitlab-runner"):
        assert File("/home/gitlab-runner/.rvm/rubies/ruby-2.4.0/bin/ruby").exists


def test_bundler_installed_with_rvm(File, Sudo):
    with Sudo("gitlab-runner"):
        assert File("/home/gitlab-runner/.rvm/gems/ruby-2.4.0/bin/bundle").exists


def test_git_configured(Command, Sudo):
    with Sudo("gitlab-runner"):
        # With Sudo() but without --git-dir, git tries to read pwd, doesn't
        # have permissions, and aborts.
        git_config_list = Command.check_output("git --git-dir=/tmp config -l")
    assert "GPII Bot" in git_config_list


def test_ssh_known_hosts_configured(File, Sudo):
    with Sudo():
        ff = File("/home/gitlab-runner/.ssh/known_hosts")
        # Existence check seems superfluous but it produces a more helpful
        # error message than .contains() when file does not exist.
        assert ff.exists
        assert ff.contains("github.com")


def test_ssh_config_configured(File, Sudo):
    with Sudo():
        ff = File("/home/gitlab-runner/.ssh/config")
        # Existence check seems superfluous but it produces a more helpful
        # error message than .contains() when file does not exist.
        assert ff.exists
        assert ff.contains("github.com")
