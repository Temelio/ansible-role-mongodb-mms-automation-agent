# mongodb-mms-automation-agent

[![Build Status](https://travis-ci.org/Temelio/ansible-role-mongodb-mms-automation-agent.svg?branch=master)](https://travis-ci.org/Temelio/ansible-role-mongodb-mms-automation-agent)

Install mongodb-mms-automation-agent package.

## Requirements

This role requires Ansible 2.4, 2.5, 2.6,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Local and Travis tests run tests on Docker by default.
See molecule documentation to use other backend.

Currently, tests are done on:
- Ubuntu Xenial
- Ubuntu Bionic

and use:
- Ansible 2.4.x
- Ansible 2.5.x
- Ansible 2.5.x


unning tests

#### Using Docker driver

```
$ tox
```

## Role Variables

### Default role variables

``` yaml
# Defaults vars file for mongodb-mms-automation-agent role

is_initd_managed_system: "{{ _is_initd_managed_system | default(False) }}"
is_systemd_managed_system: "{{ _is_systemd_managed_system | default(False) }}"

mongodb_mms_auto_agent_service_systemd:
  - src: "{{ role_path }}/templates/services/systemd.service.j2"
    dest: "{{ mongodb_mms_auto_agent_base_folders_paths.systemd }}/{{ mongodb_mms_auto_agent_service_name }}.service"
    options:
      Unit:
        Description: 'MongoDB Automation Agent for OPS manager'
        Wants: 'network.target'
      Service:
        Type: 'simple'
        User: "{{ mongodb_mms_auto_agent_user }}"
        PIDFile: "{{ mongodb_mms_auto_agent_base_folders_paths.pid }}"
        ExecStart: "/opt/mongodb-mms-automation/bin/{{ mongodb_mms_auto_agent_service_name }} -f {{ mongodb_mms_auto_agent_base_folders_paths.etc}}/automation-agent.config"
      Install:
        WantedBy: 'multi-user.target'
mongodb_mms_auto_agent_service_initd:
  - src: "{{ role_path }}/templates/init.d.j2"
    dest: "{{ mongodb_mms_auto_agent_base_folders_paths.initd }}/{{ mongodb_mms_auto_agent_service_name }}"

# Use to test syntax and feature without configure an OPS Manager instance
# Set to false on public testing
mongodb_mms_auto_agent_install_package: True

# General
mongodb_mms_auto_agent_data_path: '/data'
mongodb_mms_auto_agent_user: 'mongodb'
mongodb_mms_auto_agent_group: 'mongodb'
mongodb_mms_auto_agent_python_binary: "{{ _mongodb_mms_auto_agent_python_binary | default('/usr/bin/python2.7') }}"
mongodb_mms_auto_agent_force_curl_usage: False

# Packages
mongodb_mms_auto_agent_get_package_from_url: True
mongodb_mms_auto_agent_manager_url: "{{ _mongodb_mms_auto_agent_manager_url | default('') }}"
mongodb_mms_auto_agent_package_name: "{{ _mongodb_mms_auto_agent_package_name }}"
mongodb_mms_auto_agent_package_path: "{{ mongodb_mms_auto_agent_base_folders_paths.tmp }}/{{ mongodb_mms_auto_agent_package_name }}"
mongodb_mms_auto_agent_package_url: "{{ mongodb_mms_auto_agent_manager_url }}/download/agent/automation/{{ mongodb_mms_auto_agent_package_name }}"
mongodb_mms_auto_agent_package_state: 'present'

# Paths
mongodb_mms_auto_agent_base_folders_paths:
  etc: "{{ _mongodb_mms_auto_agent_os_base_etc_path }}/mongodb-mms"
  initd: "{{ _mongodb_mms_auto_agent_os_base_initd_path }}"
  systemd: "{{ _mongodb_mms_auto_agent_os_base_systemd_path }}"
  tmp: "{{ _mongodb_mms_auto_agent_os_base_tmp_path }}"
  pid: '/var/lib/mongodb-mms-automation/automation-agent.pid'

# Configuration
mongodb_mms_auto_agent_group_id: ''
mongodb_mms_auto_agent_api_key: ''
mongodb_mms_auto_agent_base_url: "{{ mongodb_mms_auto_agent_manager_url }}"

# Services management
mongodb_mms_auto_agent_service_name: "{{ _mongodb_mms_auto_agent_service_name }}"
mongodb_mms_auto_agent_service_state: 'started'
mongodb_mms_auto_agent_service_enabled: True
```

## How ...

### Test with an existing instance of MongoDB OPS Manager

You need to set these environment variables:
* MONGODB_MMS_AUTO_AGENT_INSTALL
* MONGODB_MMS_AUTO_AGENT_MANAGER_URL
* MONGODB_MMS_AUTO_AGENT_PACKAGE_NAME
* MONGODB_MMS_AUTO_AGENT_GROUP_ID
* MONGODB_MMS_AUTO_AGENT_API_KEY

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
update: Lise Machetel (for Temelio company)
- http://www.temelio.com
