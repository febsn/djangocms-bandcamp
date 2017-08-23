# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
import six

from .conf import settings

class BandcampAlbumPlugin(CMSPlugin):
    album_id = models.BigIntegerField(verbose_name=_('Bandcamp Album ID'))
    url = models.URLField(verbose_name=_('Bandcamp Album URL'))
    title = models.CharField(max_length=512, verbose_name=_('title'))
    bgcol = models.CharField(max_length=6, blank=True, verbose_name=_('background color (hex)'),
        help_text=_('Leave blank to use default.'))
    linkcol = models.CharField(max_length=6, blank=True, verbose_name=_('link color (hex)'),
        help_text=_('Leave blank to use default.'))
    layout = models.CharField(max_length=64, verbose_name=_('layout'),
        choices=settings.DJANGOCMS_BANDCAMP_ALBUM_LAYOUT_CHOICES,
        default=settings.DJANGOCMS_BANDCAMP_ALBUM_LAYOUT_DEFAULT)
    height = models.CharField(max_length=16, verbose_name=_('height'), blank=True,
        help_text=_('Leave blank to use default.'))

    def get_embed_url(self):
        url = "{base_url}album={album}/bgcol={bgcol}/linkcol={linkcol}/transparent=true/".format(
            base_url=settings.DJANGOCMS_BANDCAMP_BASE_URL,
            album=self.album_id,
            bgcol=self.bgcol or settings.DJANGOCMS_BANDCAMP_BGCOL_DEFAULT,
            linkcol=self.linkcol or settings.DJANGOCMS_BANDCAMP_LINKCOL_DEFAULT
        )
        url = url + "/".join([
            "{}={}".format(attr, val)
            for attr, val
            in six.iteritems(settings.DJANGOCMS_BANDCAMP_ALBUM_LAYOUTS[self.layout])
        ])
        return url

    def get_height(self):
        return self.height or settings.DJANGOCMS_BANDCAMP_HEIGHT_DEFAULT

    def __str__(self):
        return self.title
