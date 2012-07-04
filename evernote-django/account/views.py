from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from urllib import urlencode

def login_page(request):
    next_page = request.GET.get('next')
    if next_page is None:
        next_page = reverse('notes.views.home', args=[])
    if request.user.is_authenticated():
        return HttpResponseRedirect(next_page)
    return render_to_response('login.html', { 'redirect_to': next_page},
        context_instance=RequestContext(request))

def auth(request):
    username = request.REQUEST.get('username')
    password = request.REQUEST.get('password')
    user = authenticate(username=username, password=password)
    redirect_to = request.REQUEST.get('next')
    if redirect_to is None:
        redirect_to = reverse('notes.views.home', args=[])
    if user is not None:
        messages.info(request, "Logged in as %s" % username)
        login(request, user)
        return HttpResponseRedirect(redirect_to)
    else:
        messages.error(request, "Could not log you in as %s" % username)
    next_url = reverse('account.views.login_page', args=[])
    if request.GET.get('next') is not None:
        next_url += "?%s" % urlencode(dict(next=redirect_to))
    return HttpResponseRedirect(next_url)

def logout_page(request):
    logout(request)
    messages.info(request, "Successfully logged out")
    return HttpResponseRedirect(reverse('account.views.login_page',
        args=[]))
