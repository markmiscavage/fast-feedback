import os

from fabric.api import env, task, sudo

from fab_deploy2 import *
from fab_deploy2.amazon.ubuntu import *
from fabric.api import local as local_call
import logging

logger = logging.getLogger(__name__)

env.allow_agent = True

class Dev(servers.DevServer):
    git_branch = 'develop'

    def _update_server(self, *args, **kwargs):
        functions.render_template("nginx/dev-passwd")
        functions.execute_on_host('utils.install_package',
                                  package_name='postgresql-server-dev-all')
        functions.execute_on_host('utils.install_package',
                                  package_name='python-dev')
        super(Dev, self)._update_server(*args, **kwargs)

    def _setup_database(self):
        functions.execute_on_host('postgres.master_setup', db_version='9.5',
                                  section=self.config_section)


Dev().as_tasks(parent=servers, name="dev_server")


setup_env(os.path.abspath(os.path.dirname(__file__)))

env.context['dev-server'] = {
    'newrelic': {
        'environment': 'dev-server',
    },
    'nginx': {
        'client_max_body_size': '1m',
    },
    'postgres': {
        'version': '9.5',
    },
}
