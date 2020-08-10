from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = """
lookup: python_path
author: Andrew Garner
version_added: "0.1"
short_description: returns the python executable path
description:
    - This lookup returns the path to the python executable running Ansible.
"""
import sys

from ansible.plugins.lookup import LookupBase
from ansible.module_utils._text import to_text


class LookupModule(LookupBase):
    def run(self, terms, variables=None, **kwargs):
        return [to_text(sys.executable)]
