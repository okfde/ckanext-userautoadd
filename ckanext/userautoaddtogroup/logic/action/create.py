import pylons.config as config

import ckan.logic as logic
from ckan.logic.action.create import user_create as ckan_user_create
import ckan.plugins.toolkit as toolkit


def user_create(context, data_dict):
    user = ckan_user_create(context, data_dict)

    group_name = config.get('ckan.userautoaddtogroup.group_name', '')
    role = config.get('ckan.userautoaddtogroup.group_role', '')

    try:
        toolkit.get_action('group_show')(
            context, {
                'id': group_name,
            }
        )
    except logic.NotFound:
        return user

    toolkit.get_action('group_member_create')(
        context, {
            'id': group_name,
            'username': user['name'],
            'role': role,
        }
    )

    return user
