ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: python_path
short_description: returns the python executable path
version_added: "2.9"
description:
    - "This module returns the path to the python executable running Ansible on the target host."
author:
    - Andrew Garner
'''

EXAMPLES = '''
- name: Print the python interpreter path used on all target
  python_path:
'''

RETURN = '''
python_path:
    description: The path to the python executable running Ansible on the target host
    type: str
    returned: always
'''

import sys

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_text


def run_module():
    module_args = {}

    result = dict(
        changed=False,
        python_path=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    result['python_path'] = to_text(sys.executable)
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
