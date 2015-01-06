# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingData', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('match_number', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gmail_message_id', models.BigIntegerField(default=0)),
                ('sender_phone_number', models.IntegerField(default=9999999999)),
                ('message_body', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PerMatchTeamData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('team_number', models.IntegerField(default=0)),
                ('alliance_color', models.CharField(max_length=4, choices=[(b'red', b'Red'), (b'blue', b'Blue')])),
                ('kills', models.IntegerField(default=0)),
                ('deaths', models.IntegerField(default=0)),
                ('assists', models.IntegerField(default=0)),
                ('is_from_google_voice', models.BooleanField(default=True)),
                ('match_fk', models.ForeignKey(to='scoutingData.Match')),
                ('source_mail', models.ForeignKey(to='scoutingData.Message')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='match',
            name='blue_alliance_data',
            field=models.ForeignKey(related_name='+', to='scoutingData.PerMatchTeamData'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='match',
            name='red_alliance_data',
            field=models.ForeignKey(related_name='+', to='scoutingData.PerMatchTeamData'),
            preserve_default=True,
        ),
    ]
