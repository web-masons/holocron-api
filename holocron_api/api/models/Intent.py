from django.db import models
from standard import Placement


class Intent(models.Model):
    intent_key = models.SlugField(primary_key=True)
    intent_description = models.CharField(max_length=140)
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    placements = models.ManyToManyField(Placement)

    def __str__(self):
        return self.intent_key