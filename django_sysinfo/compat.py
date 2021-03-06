# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import logging

import django

from django_sysinfo.utils import get_package_version

logger = logging.getLogger(__name__)

if django.VERSION[1] in [7, 8, 9, 10, 11]:
    from django.apps import apps

    def get_installed_apps():
        installed_apps = []
        for app_config in apps.get_app_configs():
            installed_apps.append([app_config.name,
                                   get_package_version(app_config.name, app_config.module)])
        return sorted(installed_apps)

else:  # pragma: no cover
    raise EnvironmentError('Django version not supported')
