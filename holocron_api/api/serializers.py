from rest_framework import serializers
from api.models import Campaign
from api.models import Medium
from api.models import Source
from api.models import Content
from api.models import Placement


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign


class MediumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medium


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content


class PlacementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Placement


class PlacementDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Placement
        depth = 1
