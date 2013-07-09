# Create your views here.
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from polls.models import Choice, Poll #, Page

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'
    
    def get_queryset(self):
        """Return the last five published polls (not including those set to be
        published in the future).
        """
        return Poll.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]
    
class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'
    
    def get_queryset(self):
        """
        Excludes any polls that aren't published yet.
        """
        return Poll.objects.filter(pub_date__lte=timezone.now())
    
def results(request):
    '''
    Displays the results of the poll and the value of the selected {{ choice.result|safe }}
    '''

    current_url = request.path

    # Get current poll from url and set poll = to the poll object
    poll = None
    # Do string manipulation here to pull out the choice number, then set choice = choice object
    choice = None

    # Check that the choice goes with the poll and redirect to polls/detail.html if it doesn't.

    template_name = 'polls/results.html'
    return render_to_response(template_name, { 'poll' : poll, 'choice' : choice }, context_instance=RequestContext(request))
    
#class PageView(generic.DetailView):
#    model = Page
#    template_name = 'polls/page.html'
    
def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        request.session['choice'] = selected_choice
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents the data from being posted twice if a
        # user hits the Back button. 
        return HttpResponseRedirect(reverse('polls:results', kwargs={'pk': p.id,'choice': selected_choice.id } ))

