from api.models import Source, Medium, Campaign, Creative, Placement, LOB, Intent, LifeCycle, Audience
from rest_framework import viewsets
from api.serializers import SourceSerializer, MediumSerializer, \
    CampaignSerializer, CreativeSerializer, PlacementSerializer, \
    PlacementDetailsSerializer, LOBSerializer, IntentSerializer, \
    AudienceSerializer, LifeCycleSerializer


class CampaignViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Campaigns to be viewed or edited.
    """
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer


class MediumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Mediums to be viewed or edited.
    """
    queryset = Medium.objects.all()
    serializer_class = MediumSerializer


class SourceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Sources to be viewed or edited.
    """
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class CreativeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Content to be viewed or edited.
    """
    queryset = Creative.objects.all()
    serializer_class = CreativeSerializer

class LOBViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Line of Business to be viewed or edited.
    """
    queryset = LOB.objects.all()
    serializer_class = LOBSerializer

class IntentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Content to be viewed or edited.
    """
    queryset = Intent.objects.all()
    serializer_class = IntentSerializer

class LifeCycleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Content to be viewed or edited.
    """
    queryset = LifeCycle.objects.all()
    serializer_class = LifeCycleSerializer

class AudienceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Content to be viewed or edited.
    """
    queryset = Audience.objects.all()
    serializer_class = AudienceSerializer


class PlacementViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Placements (with Foreign Keys)
    to be viewed or edited.
    """
    queryset = Placement.objects.all()
    serializer_class = PlacementSerializer


class PlacementDetailsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Placements (with nested JSON)
    to be viewed or edited.
    """
    queryset = Placement.objects.all()
    serializer_class = PlacementDetailsSerializer
