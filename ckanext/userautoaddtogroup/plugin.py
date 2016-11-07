import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

import ckanext.userautoaddtogroup.logic.action.create


class UserautoaddtogroupPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IActions)

    # IConfigurer
    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'userautoaddtogroup')

    # IActions
    def get_actions(self):
        return {
            'user_create':
            ckanext.userautoaddtogroup.logic.action.create.user_create,
        }
