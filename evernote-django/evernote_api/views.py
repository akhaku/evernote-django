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
        profile = request.user.profile
        try:
            expires_time = datetime.fromtimestamp(int(credentials['expires']))
        except TypeError:
            logging.error("Error parsing token expires time")
            expires_time = datetime.now()
        profile.evernote_token = credentials['oauth_token']
        profile.evernote_token_expires_time = expires_time
        profile.evernote_shard = credentials['edam_shard']
        profile.evernote_uid = credentials['edam_userId']
        profile.save()
    return HttpResponseRedirect(settings.EVERNOTE_OAUTH_COMPLETE_URL)
