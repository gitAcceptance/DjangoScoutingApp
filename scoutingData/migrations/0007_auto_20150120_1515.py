# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingData', '0006_team_time_of_last_submission'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='avg_assists',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='team',
            name='avg_deaths',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='team',
            name='avg_kills',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
