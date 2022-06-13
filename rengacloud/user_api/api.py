"""
This is the people module and supports all the REST actions for the
people data
"""
import os, subprocess
import json
from pathlib import Path
from flask import make_response, abort
from config import db, multi_auth, basic_auth, token_auth, users, tokens, app
from werkzeug.security import check_password_hash, generate_password_hash
from flask import jsonify

def executeOccCommand(command):
    cmd = 'docker exec -it --user www-data fpm_app_1 php occ {cmd}'.format(cmd=command).split()
    process = subprocess.Popen(cmd,
                     stdout=subprocess.PIPE, 
                     stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout.strip()

@multi_auth.login_required
def group_list():
    """
    This function responds to a request for /api/groups
    with the complete lists of agents

    :return:        json string of list of agents
    """
    
    out = executeOccCommand("group:list --output=json")
    #out = "{admin:[admin]}"
    return make_response(jsonify(out), 200)
    #return out


@multi_auth.login_required
def read_group(group_name):
    """
    This function responds to a request for /api/groups/{group_name}
    with one matching group from group list

    :param person_id:   Name of group to find
    :return:            group matching name
    """
    out = executeOccCommand("groupquota:get {name} --output='json_pretty'".format(name=group_name))    
    return out 


@multi_auth.login_required
def create_group(group):
    """
    This function creates a new group in the group structure
    based on the passed in group data

    :param group:  group to create in group structure
    :return:        201 on success, 406 on group exists
    """
    return ""

		
@multi_auth.login_required
def update_group(name, group):
    """
    This function updates an existing group in the group structure
    Throws an error if a group with the name we want to update to
    already exists in the database.

    :param group_name: Name of the group to update
    :param group:      group to update
    :return:           updated group structure
    """
    return ""


@multi_auth.login_required
def delete_group(group_name):
    """
    This function deletes an group 

    :param agent_id:   Name of the group to delete
    :return:            200 on successful delete, 404 if not found
    """
    return ""


@multi_auth.login_required		
def enable_group(group_name):
    """
    This function enable an group 

    :param agent_id:   Name of the group to start
    :return:            200 on successful, 404 if not found, 500 otherwise
    """
    return ""


@multi_auth.login_required
def disable_group(group_name):
    """
    This function disable a group 

    :param agent_id:   Name of the group to stop
    :return:            200 on successful, 404 if not found, 500 otherwise
    """
    return ""

@multi_auth.login_required		
def enable_user(user_name):
    """
    This function enable an user 

    :param user_name:   Name of the user to start
    :return:            200 on successful, 404 if not found, 500 otherwise
    """
    return ""


@multi_auth.login_required
def disable_user(user_name):
    """
    This function disable an user 

    :param user_name:   Name of the user to disable
    :return:            200 on successful, 404 if not found, 500 otherwise
    """
    return ""


