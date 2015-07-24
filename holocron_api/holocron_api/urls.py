from django.conf.urls import include, url
from rest_framework import routers
from api.views import *  # noqa
from blacklist_manager.views import *  # noqa

router = routers.DefaultRouter()
router.register(r'program', ProgramViewSet)
router.register(r'campaign', CampaignViewSet)
router.register(r'tactic', TacticViewSet)
router.register(r'medium', MediumViewSet)
router.register(r'source', SourceViewSet)
router.register(r'creative', CreativeViewSet)
router.register(r'lob', LOBViewSet)
router.register(r'intent', IntentViewSet)
router.register(r'lifecycle', LifeCycleViewSet)
router.register(r'audience', AudienceViewSet)
router.register(r'lob-xref', LOB_xref_ViewSet)
router.register(r'intent-xref', Intent_xref_ViewSet)
router.register(r'lifecycle-xref', LifeCycle_xref_ViewSet)
router.register(r'audience-xref', Audience_xref_ViewSet)
router.register(r'ad-network', Ad_Network_ViewSet)
router.register(r'placement', PlacementViewSet, 'Placment')
router.register(r'blacklist/rules', BlacklistEntryViewSet)
router.register(r'blacklist', EntryViewSet)
router.register(r'export/json', ExportJSONPlacementViewSet, 'Export Json')
router.register(r'export/csv', ExportCSVPlacementViewSet, 'Export CSV')


urlpatterns = [
    url(r'^', include(router.urls))
]
