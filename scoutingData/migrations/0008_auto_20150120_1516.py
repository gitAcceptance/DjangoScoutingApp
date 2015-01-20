# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingData', '0007_auto_20150120_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='avg_assists',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='team',
            name='avg_deaths',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='team',
            name='avg_kills',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
