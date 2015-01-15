import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
    	return self.question_text

    def was_published_recently(self):
        now = timezone.now()
    	return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
    	return self.choice_text

class Message(models.Model):
    gmail_message_id = models.CharField(max_length=64, primary_key=True)
    sender_phone_number = models.IntegerField(default=9999999999)
    message_body = models.CharField(max_length=256)

    def __str__(self):
        return self.gmail_message_id

class PerMatchTeamData(models.Model):
    ALLIANCE_CHOICES = (
            ('red', 'Red'),
            ('blue', 'Blue'),
    )
    source_mail = models.ForeignKey(Message)
    team = models.IntegerField(default=0)
    match_fk = models.ForeignKey('Match')
    alliance_color = models.CharField(choices=ALLIANCE_CHOICES, max_length=4)
    kills = models.IntegerField(default=0)
    deaths = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    is_from_google_voice = models.BooleanField(default=True)

    class Meta:
        verbose_name = "PerMatchTeamData"
        verbose_name_plural = "PerMatchTeamData"

    def __str__(self):
        return "Match Number: %d, Team Number: %d" % (self.match_fk.match_number, self.team)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('scoutingData.views.details', args=[str(self.id)])


class Match(models.Model):
    match_number = models.IntegerField(primary_key = True)
    red_alliance_team_1 = models.ForeignKey(PerMatchTeamData, related_name='+', null=True)
    red_alliance_team_2 = models.ForeignKey(PerMatchTeamData, related_name='+', null=True)
    red_alliance_team_3 = models.ForeignKey(PerMatchTeamData, related_name='+', null=True)
    blue_alliance_team_1 = models.ForeignKey(PerMatchTeamData, related_name='+', null=True)
    blue_alliance_team_2 = models.ForeignKey(PerMatchTeamData, related_name='+', null=True)
    blue_alliance_team_3 = models.ForeignKey(PerMatchTeamData, related_name='+', null=True)

    class Meta:
        verbose_name_plural = "Matches"

    def __str__(self):
        return "Match number: %d" % (self.match_number)

class Team(models.Model):
    team_number = models.IntegerField(primary_key=True)
    # I'll add some metrics to track here later.

