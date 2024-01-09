# -*- coding: utf-8 -*-
#
# name:             groups.py
# author:           Valentin Dzhorov
# email:            vdzhorov@gmail.com
# created on:       09/1/2024
#

"""
cloudns_api.groups
~~~~~~~~~~~~~~~~

This module contains API wrapper functions for listing, creating, updating,
renaming, activating, and deleting groups.
"""

import requests

from .api import (
    ApiException,
    RequestResponseStub,
    api,
    get_auth_params
)
from .parameters import Parameters


@api
def list_groups():
    """Gets a list with all groups you have added for your DNS zones."""
    url = 'https://api.cloudns.net/dns/list-groups.json'

    return requests.get(url, params=get_auth_params())

@api
def change_group(domain_name=None, group_id=None):
    """Change the group which a DNS zone belongs to
    
    :param domain_name: string, domain name of the DNS zone
    :param group_id: int, ID of the relevant group
    """
    url = 'https://api.cloudns.net/dns/change-group.json'
    
    params = Parameters({'domain-name': domain_name, 'group-id': group_id})

    return requests.get(url, params=params.to_dict())

@api
def add_group(domain_name=None, name=None):
    """Create new group and add a certain DNS zone in the group instantly.
    
    :param domain_name: string, domain name you wish to add in the group
    :param name: string, name of the group
    """
    url = 'https://api.cloudns.net/dns/add-group.json'
    
    params = Parameters({'domain-name': domain_name, 'name': name})

    return requests.get(url, params=params.to_dict())

@api
def delete_group(group_id=None):
    """Delete a certain group of yours.

    :param group_id: int, ID of the relevant group 
    """
    url = 'https://api.cloudns.net/dns/delete-group.json'
    
    params = Parameters({'group-id': group_id})

    return requests.get(url, params=params.to_dict())

@api
def rename_group(group_id=None, new_name=None):
    """Rename a certain group of yours.

    :param group_id: int, ID of the relevant group
    :param new_name: string, new name for the group
    """
    url = 'https://api.cloudns.net/dns/rename-group.json'
    
    params = Parameters({'group-id': group_id, 'new-name': new_name})

    return requests.get(url, params=params.to_dict())
