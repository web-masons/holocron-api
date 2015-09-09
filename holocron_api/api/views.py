from api.models import *  # noqa
from rest_framework import viewsets
from api.serializers import *  # noqa
from rest_pandas import PandasViewSet


class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer


class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer


class TacticViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tactics to be viewed or edited.
    """
    queryset = Tactic.objects.all()
    serializer_class = TacticSerializer


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


class LOB_xref_ViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Line of Business to be viewed or edited.
    """
    queryset = LOB_xref.objects.all()
    serializer_class = LOB_xref_Serializer


class Intent_xref_ViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Content to be viewed or edited.
    """
    queryset = Intent_xref.objects.all()
    serializer_class = Intent_xref_Serializer


class LifeCycle_xref_ViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Content to be viewed or edited.
    """
    queryset = Lifecycle_xref.objects.all()
    serializer_class = LifeCycle_xref_Serializer


class Audience_xref_ViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Content to be viewed or edited.
    """
    queryset = Audience_xref.objects.all()
    serializer_class = Audience_xref_Serializer


class Ad_Network_ViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Content to be viewed or edited.
    """
    queryset = Ad_Network.objects.all()
    serializer_class = Ad_Network_Serializer


class PlacementViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Placements (with Foreign Keys)
    to be viewed or edited.
    """
    queryset = Placement.objects.all()
    serializer_class = PlacementSerializer


class ExportCSVPlacementViewSet(PandasViewSet):
    model = Placement
    queryset = Placement.objects.all()
    serializer_class = PlacementCSVExportSerializer


class ExportJSONPlacementViewSet(viewsets.ModelViewSet):
    queryset = Placement.objects.all()
    serializer_class = PlacementJSONExportSerializer
