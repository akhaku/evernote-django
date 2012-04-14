""" Most of this is modified from Hain-Lee's (leehsueh) great work at
    https://github.com/leehsueh/django-evernote-oauth/. Many many thanks to him
    for doing the legwork!
"""
from django.conf import settings
from django.http import HttpResponseRedirect
from time import time
from urllib import urlencode
import urllib2
import urlparse

class EvernoteAPI:
    evernoteHost = settings.EVERNOTE_HOST
    tempCredentialRequestUri = "https://" + evernoteHost + "/oauth"
    resOwnerAuthUri = "https://" + evernoteHost + "/OAuth.action"
    resFormat = "microclip"
    tokRequestUri = tempCredentialRequestUri
    consumerKey = settings.EVERNOTE_KEY
    consumerSecret = settings.EVERNOTE_SECRET

    userStoreUri = "https://" + evernoteHost + "/edam/user"
    noteStoreUriBase = "https://" + evernoteHost + "/edam/note/"

    def __init__(self, oauth_token=None, shard=None, uid=None, exp=None):
        self.oauth_token = oauth_token
        self.shard = shard
        self.uid = uid
        self.exp = exp

    def get_token(self, request, callback):
        request_params = dict(oauth_consumer_key = self.consumerKey,
                oauth_signature                  = self.consumerSecret,
                oauth_signature_method           = "PLAINTEXT",
                oauth_callback                   = callback,
                oauth_timestamp                  = self._get_timestamp())

        data = urlencode(request_params)
        req = urllib2.Request(self.tempCredentialRequestUri, data)
        response = urllib2.urlopen(req)
        response_params = urlparse.parse_qs(response.read())
        oauth_token = response_params['oauth_token'][0]
        oauth_callback_confirmed = response_params['oauth_callback_confirmed'][0]

        authUrl = "%s?format=%s&oauth_token=%s" % (self.resOwnerAuthUri,
                                                   self.resFormat, oauth_token)
        return HttpResponseRedirect(authUrl)

    def _get_timestamp(self):
        timestamp = int(round(time() * 1000))
        return timestamp

    def get_user_token(self, request):
        params = dict(request.GET)
        if 'oauth_token' in params.keys() and 'oauth_verifier' in params.keys():
            oauth_token = request.GET.get('oauth_token')
            oauth_verifier = request.GET.get('oauth_verifier')
            request_params = {}
            request_params['oauth_consumer_key'] = self.consumerKey
            request_params['oauth_signature'] = self.consumerSecret
            request_params['oauth_signature_method'] = 'PLAINTEXT'
            request_params['oauth_token'] = oauth_token
            request_params['oauth_verifier'] = oauth_verifier
            request_params['oauth_timestamp'] = self._get_timestamp()

            data = urlencode(request_params)
            req = urllib2.Request(self.tokRequestUri, data)
            response = urllib2.urlopen(req)

            response_params = urlparse.parse_qs(response.read())
            keys = response_params.keys()
            if 'oauth_token' in keys and 'edam_shard' in keys \
                    and 'edam_userId' in keys:
                auth_token = response_params.get('oauth_token')[0]
                edam_shard = response_params.get('edam_shard')[0]
                edam_userId = response_params.get('edam_userId')[0]
                expires = int(request_params['oauth_timestamp'])/1000 + \
                        24 * 3600 * settings.EVERNOTE_OAUTH_TOKEN_VALIDITY
                return {'oauth_token': auth_token,
                        'edam_shard': edam_shard,
                        'edam_userId': edam_userId,
                        'expires': expires}
            else:
                return None
        else:
            return None

