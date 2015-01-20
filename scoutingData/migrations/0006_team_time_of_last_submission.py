# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingData', '0005_auto_20150114_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='time_of_last_submission',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 20, 16, 58, 47, 468004, tzinfo=utc), verbose_name=b'Last Submission Time', auto_now=True),
            preserve_default=False,
        ),
    ]
