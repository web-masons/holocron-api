from django.db import models


class Ad_Network(models.Model):
    network_key = models.CharField(max_length=100, primary_key=True)
    network_description = models.CharField(max_length=140)
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.network_key
