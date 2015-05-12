from django.conf.urls import include, url
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'campaign', views.CampaignViewSet)
router.register(r'medium', views.MediumViewSet)
router.register(r'source', views.SourceViewSet)
router.register(r'content', views.ContentViewSet)
router.register(r'placement-details', views.PlacementDetailsViewSet)
router.register(r'placement', views.PlacementViewSet)


urlpatterns = [
    url(r'^', include(router.urls))
]
