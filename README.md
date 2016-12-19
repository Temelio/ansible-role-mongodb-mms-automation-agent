# mongodb-mms-automation-agent

[![Build Status](https://travis-ci.org/Temelio/ansible-role-mongodb-mms-automation-agent.svg?branch=master)](https://travis-ci.org/Temelio/ansible-role-mongodb-mms-automation-agent)

Install mongodb-mms-automation-agent package.

## Requirements

This role requires Ansible 2.0 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role has some testing methods.

To use locally testing methods, you need to install Docker and/or Vagrant and Python requirements:

* Create and activate a virtualenv
* Install requirements

```
pip install -r requirements_dev.txt
```

### Automatically with Travis

Tests runs automatically on Travis on push, release, pr, ... using docker testing containers

### Locally with Docker

You can use Docker to run tests on ephemeral containers.

```
make test-docker
```

### Locally with Vagrant

You can use Vagrant to run tests on virtual machines.

```
make test-vagrant
```

## Role Variables

### Default role variables

``` yaml
# General
mongodb_mms_auto_agent_python_binary: "{{ _mongodb_mms_auto_agent_python_binary | default('/usr/bin/python2.7') }}"

# Packages
mongodb_mms_auto_agent_get_package_from_url: True
mongodb_mms_auto_agent_package_checksum: None
mongodb_mms_auto_agent_manager_url: "{{ _mongodb_mms_auto_agent_manager_url | default('') }}"
mongodb_mms_auto_agent_package_name: "{{ _mongodb_mms_auto_agent_package_name }}"
mongodb_mms_auto_agent_package_path: "{{ mongodb_mms_auto_agent_base_folders_paths.tmp }}/{{ mongodb_mms_auto_agent_package_name }}"
mongodb_mms_auto_agent_package_url: "{{ mongodb_mms_auto_agent_manager_url }}/download/agent/automation/{{ mongodb_mms_auto_agent_package_name }}"
mongodb_mms_auto_agent_package_state: 'present'

# Paths
mongodb_mms_auto_agent_base_folders_paths:
  initd: "{{ _mongodb_mms_auto_agent_os_base_initd_path }}"
  tmp: "{{ _mongodb_mms_auto_agent_os_base_tmp_path }}"

# Services management
mongodb_mms_auto_agent_service_name: "{{ _mongodb_mms_auto_agent_service_name }}"
mongodb_mms_auto_agent_service_state: 'started'
mongodb_mms_auto_agent_service_enabled: True
mongodb_mms_auto_agent_manage_hugepage_settings: True
```

## How ...

### Test with an existing instance of MongoDB OPS Manager

You need to set these environment variables:
* MONGODB_MMS_AUTO_AGENT_INSTALL
* MONGODB_MMS_AUTO_AGENT_CHECKSUM
* MONGODB_MMS_AUTO_AGENT_MANAGER_URL

### Manage hugepage kernel settings with MongoDB recommendation

By default, this role manage these settings to set MongoDB recommendation:
* /sys/kernel/mm/transparent_hugepage/enable: never
* /sys/kernel/mm/transparent_hugepage/defrag: never

It's a new init.d service configured to start before MongoDB instances.

If you want to turn off this feature, just set mongodb_manage_hugepage_settings
to False.

## Dependencies

None

## Example Playbook

    - hosts: servers
      roles:
         - { role: Temelio.mongodb-mms-automation-agent }

## License

MIT

## Author Information

Alexandre Chaussier (for Temelio company)
- http://www.temelio.com
- alexandre.chaussier [at] temelio.com

