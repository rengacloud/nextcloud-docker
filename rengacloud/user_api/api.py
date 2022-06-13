"""
This is the people module and supports all the REST actions for the
people data
"""
import os
from pathlib import Path
from flask import make_response, abort
from config import db, multi_auth, basic_auth, token_auth, users, tokens, app
from werkzeug.security import check_password_hash, generate_password_hash

@multi_auth.login_required
def agent_list():
    """
    This function responds to a request for /api/agents
    with the complete lists of agents

    :return:        json string of list of agents
    """
    # Create the list of agents from our data
    agents = Agent.query.all()

    # Serialize the data for the response
    agent_schema = AgentSchema(many=True)
    data = agent_schema.dump(agents)
    return data


@multi_auth.login_required
def read_one(agent_id):
    """
    This function responds to a request for /api/agents/{agent_id}
    with one matching agent from agent list

    :param person_id:   Id of agent to find
    :return:            agent matching id
    """
    # Get the person requested
    # agent = Agent.query.filter(Agent.agent_id == agent_id).one_or_none()

    # # Did we find a person?
    # if agent is not None:

        # # Serialize the data for the response
        # agent_schema = AgentSchema()
        # data = agent_schema.dump(agent)
        # return data

    # # Otherwise, nope, didn't find that person
    # else:
        # abort(
            # 404,
            # "Agent not found for Id: {agent_id}".format(agent_id=agent_id),
        # )
    return ""    



    

@multi_auth.login_required
def read_one(agent_id):
    """
    This function responds to a request for /api/agents/{agent_id}
    with one matching agent from agent list

    :param person_id:   Id of agent to find
    :return:            agent matching id
    """
    return ""    	
		
@multi_auth.login_required
def group_list():
    """
    This function responds to a request for /api/groups
    with the complete lists of agents

    :return:        json string of list of agents
    """
    return ""


@multi_auth.login_required
def read_group(group_name):
    """
    This function responds to a request for /api/groups/{group_name}
    with one matching group from group list

    :param person_id:   Name of group to find
    :return:            group matching name
    """
    return ""    


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


