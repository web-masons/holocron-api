from django.db import models
from django.utils import timezone


class Campaign(models.Model):
    campaign_key = models.SlugField(max_length=100, primary_key=True)
    campaign_name = models.CharField(max_length=100)
    campaign_description = models.CharField(max_length=140)
    created_by = models.CharField(max_length=100)
    campaign_notes = models.CharField(max_length=140, blank=True)
    end_date = models.DateField('End Date')
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.campaign_key

    def still_running(self):
        return self.end_date >= timezone.now()


class Medium(models.Model):
    medium_key = models.SlugField(max_length=100, primary_key=True)
    medium_name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.medium_key


class Source(models.Model):
    source_key = models.SlugField(max_length=100, primary_key=True)
    source_name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.source_key


class Creative(models.Model):
    creative_id = models.AutoField(primary_key=True)
    creative_name = models.CharField(max_length=100)
    creative_description = models.CharField(max_length=140)
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.creative_name


class LOB(models.Model):
    lob_key = models.SlugField(primary_key=True)
    lob_description = models.CharField(max_length=140)
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.lob_key


class Intent(models.Model):
    intent_key = models.SlugField(primary_key=True)
    intent_description = models.CharField(max_length=140)
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.intent_key


class LifeCycle(models.Model):
    lifecycle_key = models.SlugField(primary_key=True)
    lifecycle_description = models.CharField(max_length=140)
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.lifecycle_key


class Audience(models.Model):
    audience_key = models.SlugField(primary_key=True)
    audience_description = models.CharField(max_length=140)
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.audience_key


class Placement(models.Model):
    placement_id = models.AutoField(primary_key=True)
    placement_name = models.CharField(max_length=100)
    placement_url = models.CharField(max_length=100)
    catid = models.IntegerField(blank=True, null=True)
    end_date = models.DateField('End Date')
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    campaign = models.ForeignKey(Campaign)
    medium = models.ForeignKey(Medium)
    source = models.ForeignKey(Source)
    creative = models.ForeignKey(Creative)
    lob = models.ForeignKey(LOB, blank=True)
    intent = models.ForeignKey(Intent, blank=True)
    lifecycle = models.ForeignKey(LifeCycle, blank=True)
    audience = models.ForeignKey(Audience, blank=True)
    jira_ticket = models.CharField(max_length=20, blank=True, default="")

    def __str__(self):
        return self.placement_id

    def still_running(self):
        return self.end_date >= timezone.now()