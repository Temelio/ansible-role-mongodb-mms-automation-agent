"""
Role tests
"""
import os
import pytest

# To run all the tests on given docker images:
pytestmark = pytest.mark.docker_images(
    'infopen/ubuntu-xenial-ssh-py27:0.2.0'
)


def test_automation_agent_service_state(Service):
    """
    Test automation agent initd service state
    """

    if os.environ['MONGODB_MMS_AUTO_AGENT_INSTALL'] == 'false':
        pytest.skip('Not apply to this test environment')

    service = Service('mongodb-mms-automation-agent')

    assert service.is_enabled
    assert service.is_running


def test_agent_configuration_file(File):
    """
    Test agent configuration file management
    """

    if os.environ['MONGODB_MMS_AUTO_AGENT_INSTALL'] == 'false':
        pytest.skip('Not apply to this test environment')

    service_file = File('/etc/mongodb-mms/automation-agent.config')

    assert service_file.exists
    assert service_file.is_file
    assert service_file.user == 'mongodb'
    assert service_file.group == 'mongodb'
    assert service_file.mode == 0o500


def test_data_directory(File):
    """
    Test data directory management
    """

    if os.environ['MONGODB_MMS_AUTO_AGENT_INSTALL'] == 'false':
        pytest.skip('Not apply to this test environment')

    service_file = File('/data')

    assert service_file.exists
    assert service_file.is_directory
    assert service_file.user == 'mongodb'
    assert service_file.group == 'mongodb'
    assert service_file.mode == 0o700
