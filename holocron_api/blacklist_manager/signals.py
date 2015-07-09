from django.db.models.signals import post_save
from models import BlacklistEntry, Entries
from django.db import transaction, Error, connection
from django.utils.translation import string_concat
from netaddr import IPNetwork
from django.db.models import Q


@transaction.atomic
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
            updated_entry = Entries.objects.get(entry=i.entry)
            updated_entry.description = i.description
            updated_entry.updated_by = i.added_by
            updated_entry.related_to = string_concat(updated_entry.related_to, ', ', i.id)
            updated_entry.save()

    if i.entry_type is IP_RANGE:
        Entries.objects.all().delete()

        my_list = BlacklistEntry.objects.filter(Q(entry_type=IP_ADDRESS) | Q(entry_type=USER_AGENT))
        for item in my_list:
            obj, created = Entries.objects.get_or_create(entry_type=item.entry_type,
                                                         entry=item.entry,
                                                         description=item.description,
                                                         added_by=item.added_by,
                                                         defaults={
                                                             'related_to': item.id
                                                         })
            if not created:
                updated_entry = Entries.objects.get(entry=item.entry)
                updated_entry.description = item.description
                updated_entry.updated_by = item.added_by
                updated_entry.related_to = string_concat(updated_entry.related_to, ', ', item.id)
                updated_entry.save()

        my_list = BlacklistEntry.objects.filter(entry_type=IP_RANGE)
        for item in my_list:
            for ip in IPNetwork(item.entry):
                obj, created = Entries.objects.get_or_create(entry_type=IP_ADDRESS,
                                                             entry=ip,
                                                             defaults={
                                                                 'related_to': item.id,
                                                                 'description': item.description,
                                                                 'added_by': item.added_by,
                                                             })

                if not created:
                    updated_entry = Entries.objects.get(entry=ip)
                    updated_entry.description = item.description
                    updated_entry.updated_by = item.added_by
                    updated_entry.related_to = string_concat(updated_entry.related_to, ', ', item.id)
                    updated_entry.save()


# register the signal
post_save.connect(save_entry, sender=BlacklistEntry)