from django.conf.urls import include, url
from rest_framework import routers
from api.views import *
from blacklist_manager.views import *

router = routers.DefaultRouter()
router.register(r'api/campaign', CampaignViewSet)
router.register(r'api/medium', MediumViewSet)
router.register(r'api/source', SourceViewSet)
router.register(r'api/creative', CreativeViewSet)
router.register(r'api/lob', LOBViewSet)
router.register(r'api/intent', IntentViewSet)
router.register(r'api/lifecycle', LifeCycleViewSet)
router.register(r'api/audience', AudienceViewSet)
router.register(r'api/lob-xref', LOB_xref_ViewSet)
router.register(r'api/intent-xref', Intent_xref_ViewSet)
router.register(r'api/lifecycle-xref', LifeCycle_xref_ViewSet)
router.register(r'api/audience-xref', Audience_xref_ViewSet)
router.register(r'api/placement-details', PlacementDetailsViewSet)
router.register(r'api/placement', PlacementViewSet)
router.register(r'blacklist/blacklist-entry', BlacklistEntryViewSet)
router.register(r'blacklist/entries', EntryViewSet)


urlpatterns = [
    url(r'^', include(router.urls))
]
