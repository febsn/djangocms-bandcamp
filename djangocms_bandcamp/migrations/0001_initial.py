# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='BandcampAlbumPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, related_name='djangocms_bandcamp_bandcampalbumplugin', serialize=False, to='cms.CMSPlugin', primary_key=True)),
                ('album_id', models.BigIntegerField(verbose_name='Bandcamp Album ID')),
                ('url', models.URLField(verbose_name='Bandcamp Album URL')),
                ('title', models.CharField(verbose_name='title', max_length=512)),
                ('bgcol', models.CharField(blank=True, verbose_name='background color (hex)', help_text='Leave blank to use default.', max_length=6)),
                ('linkcol', models.CharField(blank=True, verbose_name='link color (hex)', help_text='Leave blank to use default.', max_length=6)),
                ('layout', models.CharField(verbose_name='layout', default='standard', choices=[('slim', 'slim format'), ('artwork-only', 'artwork only'), ('standard', 'standard')], max_length=64)),
                ('height', models.CharField(blank=True, verbose_name='height', help_text='Leave blank to use default.', max_length=16)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
