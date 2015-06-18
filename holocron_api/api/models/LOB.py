from django.db import models


class LOB(models.Model):
    lob_key = models.SlugField(primary_key=True)
    lob_description = models.CharField(max_length=140)
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.lob_key
