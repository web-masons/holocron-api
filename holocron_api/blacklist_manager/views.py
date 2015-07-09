from blacklist_manager.models import *  # noqa
from rest_framework import viewsets
from blacklist_manager.serializers import *  # noqa


class BlacklistEntryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows new entries to be added to the Blacklist
    """
    queryset = BlacklistEntry.objects.all()
    serializer_class = BlacklistEntrySerializer


class EntryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows new entries to be added to the Blacklist
    """
    queryset = Entries.objects.all()
    serializer_class = EntrySerializer
