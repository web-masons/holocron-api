from django.db import models
from standard import Placement


class Audience(models.Model):
    audience_key = models.SlugField(primary_key=True)
    audience_description = models.CharField(max_length=140)
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.audience_key
