import datetime

from django.db import models
from django.utils import timezone


class Campaign(models.Model):
    campaign_id = models.AutoField(primary_key=True)
    campaign_name = models.CharField(max_length=100)
    campaign_description = models.CharField(max_length=140)
    end_date = models.DateField('End Date')
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.campaign_name

    def still_running(self):
        return self.end_date >= timezone.now()


class Medium(models.Model):
    medium_id = models.AutoField(primary_key=True)
    medium_name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.medium_name


class Source(models.Model):
    source_id = models.AutoField(primary_key=True)
    source_name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.source_name


class Content(models.Model):
    content_id = models.AutoField(primary_key=True)
    content_name = models.CharField(max_length=100)
    content_description = models.CharField(max_length=140)
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content_name


class Placement(models.Model):
    placement_id = models.AutoField(primary_key=True)
    placement_name = models.CharField(max_length=100)
    placement_url = models.CharField(max_length=100)
    end_date = models.DateField('End Date')
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    campaign = models.ForeignKey(Campaign)
    medium = models.ForeignKey(Medium)
    source = models.ForeignKey(Source)
    content = models.ForeignKey(Content)

    def __str__(self):
        return self.placement_name

    def still_running(self):
        return self.end_date >= timezone.now()
