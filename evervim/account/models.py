from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile")
    evernote_token = models.CharField(blank=True, max_length=256)
    evernote_token_expires_time = models.DateTimeField(null=True, blank=True)
