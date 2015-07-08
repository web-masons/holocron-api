from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import string_concat


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
    added_by = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


def save_entry(sender, *args, **kwargs):
    IP_ADDRESS = 'IP'
    USER_AGENT = 'UA'
    IP_RANGE = 'IR'
    ENTRY_TYPE_CHOICES = (
        (IP_ADDRESS, 'Single IP Address'),
        (USER_AGENT, 'User Agent'),
        (IP_RANGE, 'Range of IP Addresses'),
    )
    i = kwargs['instance']
    if i.entry_type is IP_ADDRESS or i.entry_type is USER_AGENT:
        obj, created = Entries.objects.get_or_create(entry_type=i.entry_type,
                                                    entry=i.entry,
                                                    description=i.description,
                                                    added_by=i.added_by,
                                                    defaults={
                                                        'related_to': i.id
                                                    })
        if not created:
            new_Entry = Entries(entry_type=i.entry_type,
                                entry=i.entry,
                                description=i.description,
                                added_by=i.added_by,
                                related_to=string_concat(obj['related_to'], ",", i.id))
            new_Entry.save()
# register the signal
post_save.connect(save_entry, sender=BlacklistEntry)