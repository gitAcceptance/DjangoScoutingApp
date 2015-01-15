# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingData', '0002_auto_20150106_1103'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_number', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='match',
            name='blue_alliance_data',
        ),
        migrations.RemoveField(
            model_name='match',
            name='red_alliance_data',
        ),
        migrations.RemoveField(
            model_name='permatchteamdata',
            name='team_number',
        ),
        migrations.AddField(
            model_name='match',
            name='blue_alliance_team_1',
            field=models.ForeignKey(related_name='+', to='scoutingData.PerMatchTeamData', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='match',
            name='blue_alliance_team_2',
            field=models.ForeignKey(related_name='+', to='scoutingData.PerMatchTeamData', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='match',
            name='blue_alliance_team_3',
            field=models.ForeignKey(related_name='+', to='scoutingData.PerMatchTeamData', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='match',
            name='red_alliance_team_1',
            field=models.ForeignKey(related_name='+', to='scoutingData.PerMatchTeamData', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='match',
            name='red_alliance_team_2',
            field=models.ForeignKey(related_name='+', to='scoutingData.PerMatchTeamData', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='match',
            name='red_alliance_team_3',
            field=models.ForeignKey(related_name='+', to='scoutingData.PerMatchTeamData', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='permatchteamdata',
            name='team',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
