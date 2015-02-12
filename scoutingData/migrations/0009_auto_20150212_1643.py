# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingData', '0008_auto_20150120_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permatchteamdata',
            name='assists',
        ),
        migrations.RemoveField(
            model_name='permatchteamdata',
            name='deaths',
        ),
        migrations.RemoveField(
            model_name='permatchteamdata',
            name='kills',
        ),
        migrations.AddField(
            model_name='permatchteamdata',
            name='attempted_coop',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='permatchteamdata',
            name='auto_quality',
            field=models.CharField(default=b'bad', max_length=6, choices=[(b'bad', b'Bad'), (b'good', b'Good'), (b'great', b'Great')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='permatchteamdata',
            name='can_traverse_bump',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='permatchteamdata',
            name='completed_coop',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='permatchteamdata',
            name='date_last_changed',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 12, 21, 42, 51, 676362, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='permatchteamdata',
            name='has_autonomous',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='permatchteamdata',
            name='height_of_capped_stack',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='permatchteamdata',
            name='noodles_manipulated',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='permatchteamdata',
            name='starting_position',
            field=models.CharField(default='NA', max_length=6, choices=[(b'right', b'Right'), (b'middle', b'Middle'), (b'left', b'Left')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='permatchteamdata',
            name='totes_touched',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
