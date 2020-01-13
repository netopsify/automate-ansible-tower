# Ansible Filters

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import json


class FilterModule(object):

    def filters(self):
        return {
            'id_extractor': self.id_extractor,
        }

    def id_extractor(self, s, *argv):

        id_dict = {}

        for obj in s['results']:
            temp_dict = {}
            inventory_host = obj['item']['name']
            id_result = json.loads(obj['stdout'])
            temp_dict.update({inventory_host: id_result})
            host_id = temp_dict[inventory_host]['results'][0]['id']
            id_dict.update(
                {inventory_host: host_id})

        return id_dict
