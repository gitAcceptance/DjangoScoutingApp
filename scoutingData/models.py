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
    RED     = 'red'
    BLUE    = 'blue'
    RIGHT   = 'right'
    LEFT    = 'left'
    MIDDLE  = 'middle'
    BAD     = 'bad'
    GOOD    = 'good'
    GREAT   = 'great'
    ALLIANCE_CHOICES = (
        (RED, 'Red'),
        (BLUE, 'Blue'),
    )
    POSITION_CHOICES = (
        (RIGHT, 'Right'),
        (MIDDLE, 'Middle'),
        (LEFT, 'Left'),
    )
    QUALITY_CHOICES = (
        (BAD, 'Bad'),
        (GOOD, 'Good'),
        (GREAT, 'Great'),
    )
    date_last_changed = models.DateTimeField(auto_now=True)
    source_mail = models.ForeignKey('Message')
    is_from_google_voice = models.BooleanField(default=True)
    team = models.IntegerField(default=0)
    match_fk = models.ForeignKey('Match')
    alliance_color = models.CharField(choices=ALLIANCE_CHOICES, max_length=4)
    starting_position = models.CharField(choices=POSITION_CHOICES, max_length=6)
    # autonomous period
    has_autonomous = models.BooleanField(default=False)
    auto_quality = models.CharField(choices=QUALITY_CHOICES, max_length=6, default=BAD)
    # teleoperated period
    totes_touched = models.IntegerField(default=0)
    noodles_manipulated = models.IntegerField(default=0)
    height_of_capped_stack = models.IntegerField(default=0)
    attempted_coop = models.BooleanField(default=False)
    completed_coop = models.BooleanField(default=False)
    can_traverse_bump = models.BooleanField(default=False)


    class Meta:
        verbose_name = "PerMatchTeamData"
        verbose_name_plural = "PerMatchTeamData"

    def __str__(self):
        return "Match Number: %d, Team Number: %d" % (self.match_fk.match_number, self.team)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('scoutingData.views.details', args=[str(self.id)])

    def save(self, *args, **kwagrs):
        # implement the saving of related entrys and recalulating team metrics

        super(scoutingData, self).save(self, *args, **kwargs)

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
        return "Match number: %s" % (self.match_number)

class Team(models.Model):
    team_number = models.IntegerField(primary_key=True)
    time_of_last_submission = models.DateTimeField('Last Submission Time', auto_now=True)
    avg_kills = models.IntegerField(default=0)
    avg_deaths = models.IntegerField(default=0)
    avg_assists = models.IntegerField(default=0)
    # I'll add some metrics to track here later.
    # Don't forget that any computed metrics might not be integers
    # and as such won't like getting slotted into an Int field

    def __str__(self):
        return "Team number: %d" % (self.team_number)








