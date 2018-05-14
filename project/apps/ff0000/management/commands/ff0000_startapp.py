# vim: set fileencoding=utf-8 :
from __future__ import absolute_import, division, print_function, unicode_literals

import os
import sys
from optparse import make_option
from django.core.management.base import BaseCommand
from django.conf import settings

# Basic template for new management commands
MANAGEMENT_TEMPLATE = """from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        pass"""

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--serializers', '-s',
            action='store_true',
            help='add serializers.py file'),
        make_option('--management', '-m',
            action='store',
            help='add management commands dirs'),
    )
    help = "Create a new django app with empty files relevant to a scarlet app"


    def touch(self, fname, times=None):
        """ Emulate `touch` executable behavior.

        Parameters
        ----------
        fname : str
            Path to a file to create or update.
        times : tuple, optional
            A 2-tuple of numbers of the form `(atime, mtime)`.
            If omitted, will default to the current time.

        Notes
        -----
        Open file for append to avoid race condition.

        """
        with open(fname, 'a'):
            os.utime(fname, times)


    def handle(self, *args, **options):
        try:
            app_name = args[0]
        except IndexError:
            print('No app name provided.')
            sys.exit(1)

        new_dir = os.path.join(settings.PROJECT_ROOT, 'apps', app_name)
        if not os.path.exists(new_dir):
            os.mkdir(new_dir)

        create_files = ['__init__.py', 'models.py', 'views.py', 'cms_bundles.py', 'cache_groups.py']
        if options.get('serializers', False):
            create_files.append('serializers.py')

        for file_name in create_files:
            f = os.path.join(new_dir, file_name)
            self.touch(f)

        command_name = options.get('management', '')
        if command_name:
            management_dir = os.path.join(new_dir, 'management')
            if not os.path.exists(management_dir):
                os.mkdir(management_dir)
            self.touch(os.path.join(management_dir, '__init__.py'))

            commands_dir = os.path.join(management_dir, 'commands')
            if not os.path.exists(commands_dir):
                os.mkdir(commands_dir)
            self.touch(os.path.join(commands_dir, '__init__.py'))
            command_file = os.path.join(commands_dir, command_name)
            with open(command_file, 'w+') as f:
                print(MANAGEMENT_TEMPLATE, file=f)
