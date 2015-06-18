from django.db import models


class Intent(models.Model):
    intent_key = models.SlugField(primary_key=True)
    intent_description = models.CharField(max_length=140)
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.intent_key
