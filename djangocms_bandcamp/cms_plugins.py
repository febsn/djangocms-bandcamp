# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _

from . import models


class BandcampAlbumPlugin(CMSPluginBase):
    model = models.BandcampAlbumPlugin
    module = _("Bandcamp")
    name = _("Bandcamp Album")
    render_template = "djangocms_bandcamp/plugins/album.html"

    def render(self, context, instance, placeholder):
        context = super(BandcampAlbumPlugin, self).render(context, instance, placeholder)
        context.update({
            'instance': instance,
        })
        return context
plugin_pool.register_plugin(BandcampAlbumPlugin)
