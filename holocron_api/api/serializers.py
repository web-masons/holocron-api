from rest_framework import serializers
from api.models import Campaign
from api.models import Medium
from api.models import Source
from api.models import Creative
from api.models import LOB
from api.models import LifeCycle
from api.models import Intent
from api.models import Audience
from api.models import Placement
from django.utils.translation import string_concat


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign


class MediumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medium


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source


class CreativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creative


class LOBSerializer(serializers.ModelSerializer):
    class Meta:
        model = LOB


class LifeCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = LifeCycle


class IntentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intent


class AudienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audience


class PlacementSerializer(serializers.ModelSerializer):
    generated_url = serializers.SerializerMethodField()

    class Meta:
        model = Placement

    def get_generated_url(self, obj):
        if obj.catid is not None:
            return string_concat(obj.placement_url, "?utm_campaign=",
                                 obj.campaign, "&utm_source=", obj.source,
                                 "&utm_medium=", obj.medium, "&utm_content=",
                                 obj.placement_id, "&catid=", obj.catid,
                                 "&c3ch=", obj.medium, "&c3nid=",
                                 obj.placement_id)
        else:
            return string_concat(obj.placement_url, "?utm_campaign=",
                                 obj.campaign, "&utm_source=", obj.source,
                                 "&utm_medium=", obj.medium,
                                 "&utm_content=", obj.placement_id,
                                 "&c3ch=", obj.medium, "&c3nid=",
                                 obj.placement_id)


class PlacementDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Placement
        depth = 1
