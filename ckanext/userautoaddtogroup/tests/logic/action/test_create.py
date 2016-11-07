import nose.tools

import ckan.tests.helpers as helpers
import ckan.tests.factories as factories


class TestUserCreate(helpers.FunctionalTestBase):
    def setup(self):
        super(TestUserCreate, self).setup()
        self.admin = factories.User(name='admin')
        self.group = factories.Group(
            name='mapaction', user=self.admin)

    @classmethod
    def _apply_config_changes(cls, cfg):
        plugins = set(cfg['ckan.plugins'].strip().split())
        plugins.add('userautoaddtogroup')
        cfg['ckan.plugins'] = ' '.join(plugins)

    @helpers.change_config('ckan.userautoaddtogroup.group_name',
                           'mapaction')
    @helpers.change_config('ckan.userautoaddtogroup.group_role',
                           'editor')
    def test_new_user_added_to_group(self):
        user = helpers.call_action(
            'user_create',
            email='test@example.com',
            name='testuser',
            password='abc123')

        group = helpers.call_action(
            'group_show',
            context={'user': self.admin['name']},
            id=self.group['id'])

        group_users = {o['name']: o for o in group['users']}

        nose.tools.assert_true(user['name'] in group_users)

        group_user = group_users[user['name']]

        nose.tools.assert_equal(group_user['capacity'], 'editor')
