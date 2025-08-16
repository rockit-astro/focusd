#
# This file is part of the Robotic Observatory Control Kit (rockit)
#
# rockit is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# rockit is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with rockit.  If not, see <http://www.gnu.org/licenses/>.

"""Helper function to validate and parse the json config file"""

import json
from rockit.common import daemons, IP, validation

CONFIG_SCHEMA = {
    'type': 'object',
    'additionalProperties': False,
    'required': ['daemon', 'log_name', 'control_machines', 'serial_port', 'serial_baud', 'serial_timeout',
                 'channels', 'idle_loop_delay', 'moving_loop_delay', 'move_timeout'], # temperature_probes is optional
    'properties': {
        'daemon': {
            'type': 'string',
            'daemon_name': True
        },
        'log_name': {
            'type': 'string',
        },
        'control_machines': {
            'type': 'array',
            'items': {
                'type': 'string',
                'machine_name': True
            }
        },
        'serial_port': {
            'type': 'string',
        },
        'serial_baud': {
            'type': 'number',
            'min': 115200,
            'max': 115200
        },
        'serial_timeout': {
            'type': 'number',
            'min': 0
        },
        'channels': {
            'type': 'number',
            'min': 1
        },
        'idle_loop_delay': {
            'type': 'number',
            'min': 0
        },
        'moving_loop_delay': {
            'type': 'number',
            'min': 0
        },
        'move_timeout': {
            'type': 'number',
            'min': 0
        },
        'temperature_probes': {
            'type': 'object',
            'additionalProperties': {
                'type': 'object',
                'additionalProperties': False,
                'required': ['label', 'address'],
                'properties': {
                    'label': {
                        'type': 'string'
                    },
                    'address': {
                        'type': 'string',
                        'minLength': 16,
                        'maxLength': 16
                    }
                }
            }
        }
    }
}


class Config:
    """Daemon configuration parsed from a json file"""
    def __init__(self, config_filename):
        # Will throw on file not found or invalid json
        with open(config_filename, 'r', encoding='utf-8') as config_file:
            config_json = json.load(config_file)

        # Will throw on schema violations
        validation.validate_config(config_json, CONFIG_SCHEMA, {
            'daemon_name': validation.daemon_name_validator,
            'machine_name': validation.machine_name_validator,
        })

        self.daemon = getattr(daemons, config_json['daemon'])
        self.log_name = config_json['log_name']
        self.control_ips = [getattr(IP, machine) for machine in config_json['control_machines']]
        self.serial_port = config_json['serial_port']
        self.serial_baud = int(config_json['serial_baud'])
        self.serial_timeout = int(config_json['serial_timeout'])

        self.channels = config_json['channels']
        self.idle_loop_delay = int(config_json['idle_loop_delay'])
        self.moving_loop_delay = int(config_json['moving_loop_delay'])
        self.move_timeout = int(config_json['move_timeout'])
        self.temperature_probes = config_json.get('temperature_probes', {})
