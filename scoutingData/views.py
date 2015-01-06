
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
# from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from scoutingData.models import Question, Choice

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'scoutingData/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions.
        (not inclusding the ones set to be published in the future)
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DataListView(generic.ListView):
    model = Match
    template_name = 'scoutingData/index.html'
    context_object_name = 'latest_question_list'

    # this gmail code doesn't belong here
    def get_queryset(self):
        # Path to the client_secret.json file downloaded from the Developer Console
        CLIENT_SECRET_FILE = 'client_secret.json'

        # Check https://developers.google.com/gmail/api/auth/scopes for all available scopes
        OAUTH_SCOPE = 'https://www.googleapis.com/auth/gmail.readonly'

        # Location of the credentials storage file
        STORAGE = Storage('gmail.storage')

        # Start the OAuth flow to retrieve credentials
        flow = flow_from_clientsecrets(CLIENT_SECRET_FILE, scope=OAUTH_SCOPE)
        http = httplib2.Http()

        # Try to retrieve credentials from storage or run the flow to generate them
        credentials = STORAGE.get()
        if credentials is None or credentials.invalid:
          credentials = run(flow, STORAGE, http=http)

        # Authorize the httplib2.Http object with our credentials
        http = credentials.authorize(http)

        # Build the Gmail service from discovery
        gmail_service = build('gmail', 'v1', http=http)

        # Retrieve a page of messages
        messages = gmail_service.users().messages().list(userId='me').execute()

        
            

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
