"""
Role tests
"""
import pytest

# To run all the tests on given docker images:
pytestmark = pytest.mark.docker_images(
    'infopen/ubuntu-trusty-ssh:0.1.0',
    'infopen/ubuntu-xenial-ssh-py27:0.2.0'
)


def test_hugepage_service_file(File):
    """
    Test hugepage initd service file management
    """

    service_file = File('/etc/init.d/disable-transparent-hugepages')

    assert service_file.exists
    assert service_file.is_file
    assert service_file.user == 'root'


def test_hugepage_service_state(Service):
    """
    Test hugepage initd service state
    """

    service = Service('disable-transparent-hugepages')

    assert service.is_enabled
    assert service.is_running


def test_hugepage_setting_value(SystemInfo, File):
    """
    Test if kernel hugepage setting have recommended value
    """

    if SystemInfo.distribution != 'ubuntu':
        pytest.skip('Not apply to %s' % SystemInfo.distribution)

    setting_paths = [
        '/sys/kernel/mm/transparent_hugepage/enabled',
        '/sys/kernel/mm/transparent_hugepage/defrag',
    ]

    for setting_path in setting_paths:
        assert '[never]' in File(setting_path).content_string
