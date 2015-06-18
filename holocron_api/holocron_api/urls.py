from django.conf.urls import include, url
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'campaign', views.CampaignViewSet)
router.register(r'medium', views.MediumViewSet)
router.register(r'source', views.SourceViewSet)
router.register(r'creative', views.CreativeViewSet)
router.register(r'lob', views.LOBViewSet)
router.register(r'intent', views.IntentViewSet)
router.register(r'lifecycle', views.LifeCycleViewSet)
router.register(r'audience', views.AudienceViewSet)
router.register(r'lob-xref', views.LOB_xref_ViewSet)
router.register(r'intent-xref', views.Intent_xref_ViewSet)
router.register(r'lifecycle-xref', views.LifeCycle_xref_ViewSet)
router.register(r'audience-xref', views.Audience_xref_ViewSet)
router.register(r'placement-details', views.PlacementDetailsViewSet)
router.register(r'placement', views.PlacementViewSet)


urlpatterns = [
    url(r'^', include(router.urls))
]
