from datetime import datetime
from django.http import HttpResponseRedirect
from evernote_api import EvernoteAPI
from django.conf import settings
import logging

def get_evernote_token(request):
    """ View that handles the callback from the Evernote OAuth call and
        stores the OAuth token for the user
    """
    if request.user.is_authenticated:
        everAuth = EvernoteAPI()
        credentials = everAuth.get_user_token(request)
        """ credentials is of the form: { 'oauth_token': token,
                                          'expires'    : datetime,
                                          'edam_shard' : shard,
                                          'edam_userId': uid }
        """                        
        try:
            expires_time = datetime.fromtimestamp(int(credentials['expires']))
        except TypeError:
            logging.error("Error parsing token expires time")
            expires_time = datetime.now()
        request.session['oauth_token'] = credentials['oauth_token']
        request.session['expires'] = expires_time
        request.session['edam_shard'] = credentials['edam_shard']
        request.session['edam_userId'] = credentials['edam_userId']
    return HttpResponseRedirect(settings.EVERNOTE_OAUTH_COMPLETE_URL)
