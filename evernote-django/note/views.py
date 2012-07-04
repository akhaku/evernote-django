from datetime import datetime
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from evernote_api import EvernoteAPI
import logging

def home(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('account.views.login_page', args=[]))
    profile = request.user.profile
    try:
        profile.evernote_token = request.session['oauth_token']
        profile.evernote_token_expires_time = request.session['expires']
        profile.evernote_shard = request.session['edam_shard']
        profile.evernote_uid = request.session['edam_userId']
        profile.save()
        del request.session['oauth_token']
        del request.session['expires']
        del request.session['edam_shard']
        del request.session['edam_userId']
    except KeyError:
        pass
    if profile.evernote_token == "" \
            or profile.evernote_token_expires_time < datetime.now():
        everAuth = EvernoteAPI()
        callback_url = request.build_absolute_uri(everAuth.token_callback_url)
        return everAuth.get_token(request, callback_url)
    everAPI = EvernoteAPI(profile.evernote_token, profile.evernote_shard)
    allnotes = everAPI.get_notes_with_tag("evervim")
    allnotes = [{'title': n.title, 'id': n.guid} for n in allnotes]
    return render_to_response('home.html', {'notes': allnotes},
            context_instance=RequestContext(request))
