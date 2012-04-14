from datetime import datetime
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from evernote_api import EvernoteAPI
import logging

def home(request):
    profile = request.user.profile
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('account.views.login_page', args=[]))
    if profile.evernote_token == "" \
            or profile.evernote_token_expires_time < datetime.now():
        callback_url = request.build_absolute_uri(
                reverse('evernote_api.views.get_evernote_token', args=[]))
        everAuth = EvernoteAPI()
        return everAuth.get_token(request, callback_url)
    everAPI = EvernoteAPI(profile.evernote_token, profile.evernote_shard)
    logging.error(everAPI.get_notes_with_tag("evervim"))
    return render_to_response('home.html', {},
            context_instance=RequestContext(request))
