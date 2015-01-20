
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
# from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic import View
from django.utils import timezone
from chartit import DataPool, Chart
from scoutingData.models import Question, Choice, Team
import scoutingData.graphs

# Create your views here.

class IndexView(generic.ListView):
    model = Team
    template_name = 'scoutingData/index.html'
    context_object_name = 'team_info_list'


    def get_queryset(self):
        """Return the last five published questions.
        (not inclusding the ones set to be published in the future)
        """
        return Team.objects.filter(
            time_of_last_submission__lte=timezone.now()
        ).order_by('-time_of_last_submission')[:4]


class ShowcaseView(View):
    template_name = 'scoutingData/showcase.html'
    context_object_name = 'bigchart'

    def make_charts(self):
        for team in IndexView.get_queryset():
            chart_list.append(team_chart_view(team.team_number))
        return render_to_response({'bigchart': chart_list})



class DataListView(generic.ListView):
    #model = Match
    template_name = 'scoutingData/index.html'
    context_object_name = 'latest_question_list'

    # this gmail code doesn't belong here
    def get_queryset(self):
        # meh
        return 5



class DetailView(generic.DetailView):
    model = Question
    template_name = 'scoutingData/detail.html'

    def get_queryset(self):
        """
        Excludes stuff that isn't published yet
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'scoutingData/results.html'

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'scoutingData/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('scoutingData:results', args=(p.id,)))
