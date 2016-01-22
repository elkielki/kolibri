# -*- coding: utf-8 -*-
"""
The core app of Kolibri also uses the plugin API <3
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse


from kolibri.plugins.base import KolibriPluginBase
from kolibri.plugins.hooks import NAVIGATION_POPULATE


def main_navigation():
    """
    Callback for the plugin below
    :return: A list of nav menu items used in the NAVIGATION_POPULATE hook.
    """
    return [{
        'menu_name': _("Start page"),
        'menu_url': reverse('kolibri:index'),
    }]


class KolibriCore(KolibriPluginBase):
    """
    The most minimal plugin possible. Because it's in the core, it doesn't define ``enable`` or ``disable``. Those
    methods should never be called for this plugin.
    """
    hooks = {
        NAVIGATION_POPULATE: main_navigation
    }
