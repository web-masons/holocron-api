from django.db import models


# Create your models here.
class BlacklistEntry(models.Model):
    IP_ADDRESS = 'IP'
    USER_AGENT = 'UA'
    IP_RANGE = 'IR'
    ENTRY_TYPE_CHOICES = (
        (IP_ADDRESS, 'Single IP Address'),
        (USER_AGENT, 'User Agent'),
        (IP_RANGE, 'Range of IP Addresses'),
    )

    entry_type = models.CharField(max_length=2,
                                  choices=ENTRY_TYPE_CHOICES,
                                  default=IP_ADDRESS)
    description = models.CharField(max_length=100)
    added_by = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    entry = models.CharField(max_length=100, unique=True)


class Entries(models.Model):
    IP_ADDRESS = 'IP'
    USER_AGENT = 'UA'
    ENTRY_TYPE_CHOICES = (
        (IP_ADDRESS, 'Single IP Address'),
        (USER_AGENT, 'User Agent'),
    )
    entry_type = models.CharField(max_length=2,
                                  choices=ENTRY_TYPE_CHOICES,
                                  default=IP_ADDRESS)
    entry = models.CharField(max_length=100, unique=True)
    related_to = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    update_by = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)