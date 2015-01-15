from django.contrib import admin
from scoutingData.models import Question, Choice, Message, PerMatchTeamData, Match, Team

# Register your models here.

class ChoiceInLine(admin.StackedInline):
	model = Choice
	extra = 1

class QuestionAdmin(admin.ModelAdmin):
	fields = ['pub_date', 'question_text']
	inlines = [ChoiceInLine]
	list_filter = ['pub_date']
	search_fields = ['question_text']

"""
class MessageAdmin(admin.ModelAdmin):
	fields
"""

admin.site.register(Question, QuestionAdmin)
admin.site.register(Message)
admin.site.register(PerMatchTeamData)
admin.site.register(Match)
admin.site.register(Team)