from django.db import models
from django.contrib.auth.models import User
from django.core import validators
from django.urls import reverse


class Issue(models.Model):
    """ISSUE"""
    name = models.CharField('name', max_length=255)
    issueKey = models.CharField('issueKey', max_length=255, blank=True)
    summary = models.CharField('summary', max_length=255, blank=True)
    elapsedTime = models.CharField('elapsedTime', max_length=255, blank=True)
    modificationTimeStamp = models.DateTimeField('modificationTimeStamp', blank=True, null=True)

    def __str__(self):
        return self.name
