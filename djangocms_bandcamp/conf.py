# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from appconf import AppConf

class BandcampConf(AppConf):
    ALBUM_LAYOUTS = {
        'slim': {
            'size': 'small',
        },
        'artwork-only': {
            'size': 'large',
            'minimal': 'true',
        },
        'standard': {
            'size': 'large',
            'tracklist': 'false',
        },
        'standard-tracklist': {
            'size': 'large',
            'artwork': 'small',
        },
    }
    ALBUM_LAYOUT_CHOICES = (
        ('slim', 'slim format'),
        ('artwork-only', 'artwork only'),
        ('standard', 'standard'),
        ('standard-tracklist', 'standard with tracklist'),
    )
    ALBUM_LAYOUT_DEFAULT = 'standard'
    BGCOL_DEFAULT = 'ffffff'
    LINKCOL_DEFAULT = '0687f5'
    BASE_URL = 'https://bandcamp.com/EmbeddedPlayer/'
    HEIGHT_DEFAULT = "350px";
