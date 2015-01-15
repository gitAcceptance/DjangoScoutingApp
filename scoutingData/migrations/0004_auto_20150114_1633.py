# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingData', '0003_auto_20150114_1405'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='match',
            options={'verbose_name_plural': 'Matches'},
        ),
        migrations.AlterModelOptions(
            name='permatchteamdata',
            options={'verbose_name': 'PerMatchTeamData', 'verbose_name_plural': 'PerMatchTeamData'},
        ),
        migrations.RemoveField(
            model_name='message',
            name='id',
        ),
        migrations.AlterField(
            model_name='message',
            name='gmail_message_id',
            field=models.BigIntegerField(default=0, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
