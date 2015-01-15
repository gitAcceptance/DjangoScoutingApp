# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingData', '0004_auto_20150114_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='gmail_message_id',
            field=models.CharField(max_length=64, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
