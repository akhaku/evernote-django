from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('account.views.login_page', args=[]))
    return render_to_response('home.html', {},
            context_instance=RequestContext(request))
