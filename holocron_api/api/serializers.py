from rest_framework import serializers
from api.models import *  # noqa
from django.utils.translation import string_concat


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign


class TacticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tactic

    tactic_id = serializers.ReadOnlyField()


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


class LOB_xref_Serializer(serializers.ModelSerializer):
    class Meta:
        model = LOB_xref


class LifeCycle_xref_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Lifecycle_xref


class Intent_xref_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Intent_xref


class Audience_xref_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Audience_xref


class Ad_Network_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Ad_Network


class PlacementSerializer(serializers.ModelSerializer):
    generated_url = serializers.SerializerMethodField()

    class Meta:
        model = Placement

    def get_generated_url(self, obj):
        if obj.catid is not None:
            if (obj.page_id is not None and obj.page_id != "") and \
                    (obj.page_cat is not None and obj.page_cat != ""):
                return string_concat(obj.placement_url, "?utm_campaign=",
                                     obj.tactic.tactic_key,
                                     "&utm_source=", obj.source,
                                     "&utm_medium=", obj.medium,
                                     "&utm_content=", obj.placement_id,
                                     "&catid=", obj.catid,
                                     "&c3placement=", obj.placement_id,
                                     "&cm_mmc=", obj.medium, "-_-",
                                     obj.source, "-_-", obj.placement_id,
                                     "-_-", obj.creative.creative_id,
                                     "&Category=", obj.page_cat,
                                     "&Page_ID=", obj.page_id)

            else:
                return string_concat(obj.placement_url, "?utm_campaign=",
                                     obj.tactic.tactic_key,
                                     "&utm_source=",  obj.source,
                                     "&utm_medium=",  obj.medium,
                                     "&utm_content=", obj.placement_id,
                                     "&catid=", obj.catid,
                                     "&c3placement=", obj.placement_id,
                                     "&cm_mmc=", obj.medium, "-_-",
                                     obj.source, "-_-", obj.placement_id,
                                     "-_-", obj.creative.creative_id)
        else:
            if (obj.page_id is not None and obj.page_id != "") and \
                    (obj.page_cat is not None and obj.page_cat != ""):
                return string_concat(obj.placement_url, "?utm_campaign=",
                                     obj.tactic.tactic_key,
                                     "&utm_source=", obj.source,
                                     "&utm_medium=", obj.medium,
                                     "&utm_content=", obj.placement_id,
                                     "&c3placement=", obj.placement_id,
                                     "&cm_mmc=", obj.medium, "-_-",
                                     obj.source, "-_-", obj.placement_id,
                                     "-_-", obj.creative.creative_id,
                                     "&Category=", obj.page_cat,
                                     "&Page_ID=", obj.page_id)

            else:
                return string_concat(obj.placement_url, "?utm_campaign=",
                                     obj.tactic.tactic_key,
                                     "&utm_source=", obj.source,
                                     "&utm_medium=", obj.medium,
                                     "&utm_content=", obj.placement_id,
                                     "&c3placement=", obj.placement_id,
                                     "&cm_mmc=", obj.medium, "-_-",
                                     obj.source, "-_-", obj.placement_id,
                                     "-_-", obj.creative.creative_id)


class PlacementJSONExportSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Placement
        depth = 3


class PlacementCSVExportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Placement

    id = serializers.SerializerMethodField()
    tactic_key = serializers.SerializerMethodField()
    tactic_name = serializers.SerializerMethodField()
    tactic_description = serializers.SerializerMethodField()
    tactic_notes = serializers.SerializerMethodField()
    tactic_start_date = serializers.SerializerMethodField()
    tactic_end_date = serializers.SerializerMethodField()
    tactic_created_by = serializers.SerializerMethodField()
    tactic_created_on = serializers.SerializerMethodField()
    tactic_updated_on = serializers.SerializerMethodField()
    campaign = serializers.SerializerMethodField()
    campaign_description = serializers.SerializerMethodField()
    campaign_notes = serializers.SerializerMethodField()
    campaign_start_date = serializers.SerializerMethodField()
    campaign_end_date = serializers.SerializerMethodField()
    campaign_created_by = serializers.SerializerMethodField()
    campaign_created_on = serializers.SerializerMethodField()
    campaign_updated_on = serializers.SerializerMethodField()
    program = serializers.SerializerMethodField()
    program_description = serializers.SerializerMethodField()
    program_notes = serializers.SerializerMethodField()
    program_start_date = serializers.SerializerMethodField()
    program_end_date = serializers.SerializerMethodField()
    program_created_by = serializers.SerializerMethodField()
    program_created_on = serializers.SerializerMethodField()
    program_updated_on = serializers.SerializerMethodField()
    medium_name = serializers.SerializerMethodField()
    medium_created_on = serializers.SerializerMethodField()
    medium_updated_on = serializers.SerializerMethodField()
    source_name = serializers.SerializerMethodField()
    source_created_on = serializers.SerializerMethodField()
    source_updated_on = serializers.SerializerMethodField()
    creative_key = serializers.SerializerMethodField()
    creative_name = serializers.SerializerMethodField()
    creative_created_on = serializers.SerializerMethodField()
    creative_updated_on = serializers.SerializerMethodField()
    ad_network_description = serializers.SerializerMethodField()
    ad_network_created_on = serializers.SerializerMethodField()
    ad_network_updated_on = serializers.SerializerMethodField()
    audience_key = serializers.SerializerMethodField()
    audience_description = serializers.SerializerMethodField()
    audience_created_on = serializers.SerializerMethodField()
    audience_updated_on = serializers.SerializerMethodField()
    intent_key = serializers.SerializerMethodField()
    intent_description = serializers.SerializerMethodField()
    intent_created_on = serializers.SerializerMethodField()
    intent_updated_on = serializers.SerializerMethodField()
    lifecycle_key = serializers.SerializerMethodField()
    lifecycle_description = serializers.SerializerMethodField()
    lifecycle_created_on = serializers.SerializerMethodField()
    lifecycle_updated_on = serializers.SerializerMethodField()
    lob_key = serializers.SerializerMethodField()
    lob_description = serializers.SerializerMethodField()
    lob_created_on = serializers.SerializerMethodField()
    lob_updated_on = serializers.SerializerMethodField()

    def get_id(self, obj):
        return obj.placement_id

    def get_tactic_key(self, obj):
        return obj.tactic.tactic_key

    def get_tactic_name(self, obj):
        return obj.tactic.tactic_name

    def get_tactic_description(self, obj):
        return obj.tactic.tactic_description

    def get_tactic_notes(self, obj):
        return obj.tactic.tactic_notes

    def get_tactic_start_date(self, obj):
        return obj.tactic.start_date

    def get_tactic_end_date(self, obj):
        return obj.tactic.end_date

    def get_tactic_created_by(self, obj):
        return obj.tactic.created_by

    def get_tactic_created_on(self, obj):
        return obj.tactic.created_on

    def get_tactic_updated_on(self, obj):
        return obj.tactic.updated

    def get_campaign(self, obj):
        return obj.tactic.campaign

    def get_campaign_description(self, obj):
        return obj.tactic.campaign.campaign_description

    def get_campaign_notes(self, obj):
        return obj.tactic.campaign.campaign_notes

    def get_campaign_start_date(self, obj):
        return obj.tactic.campaign.start_date

    def get_campaign_end_date(self, obj):
        return obj.tactic.campaign.end_date

    def get_campaign_created_by(self, obj):
        return obj.tactic.campaign.created_by

    def get_campaign_created_on(self, obj):
        return obj.tactic.campaign.created_on

    def get_campaign_updated_on(self, obj):
        return obj.tactic.campaign.updated

    def get_program(self, obj):
        return obj.tactic.campaign.program

    def get_program_description(self, obj):
        return obj.tactic.campaign.program.program_description

    def get_program_notes(self, obj):
        return obj.tactic.campaign.program.program_notes

    def get_program_start_date(self, obj):
        return obj.tactic.campaign.program.start_date

    def get_program_end_date(self, obj):
        return obj.tactic.campaign.program.end_date

    def get_program_created_by(self, obj):
        return obj.tactic.campaign.program.created_by

    def get_program_created_on(self, obj):
        return obj.tactic.campaign.program.created_on

    def get_program_updated_on(self, obj):
        return obj.tactic.campaign.program.updated

    def get_medium_name(self, obj):
        return obj.medium.medium_name

    def get_medium_created_on(self, obj):
        return obj.medium.created_on

    def get_medium_updated_on(self, obj):
        return obj.medium.updated

    def get_source_name(self, obj):
        return obj.source.source_name

    def get_source_created_on(self, obj):
        return obj.source.created_on

    def get_source_updated_on(self, obj):
        return obj.source.updated

    def get_creative_key(self, obj):
        return obj.creative.creative_description

    def get_creative_name(self, obj):
        return obj.creative.creative_name

    def get_creative_created_on(self, obj):
        return obj.creative.created_on

    def get_creative_updated_on(self, obj):
        return obj.creative.updated

    def retrieve_ad_network(self, obj):
        try:
            net = Ad_Network.objects.get(network_key=obj.ad_network)
            return net
        except:
            return False

    def get_ad_network_description(self, obj):
        net = self.retrieve_ad_network(obj)
        if net:
            return obj.ad_network.network_description
        else:
            return None

    def get_ad_network_created_on(self, obj):
        net = self.retrieve_ad_network(obj)
        if net:
            return obj.ad_network.created_on
        else:
            return None

    def get_ad_network_updated_on(self, obj):
        net = self.retrieve_ad_network(obj)
        if net:
            return obj.ad_network.updated
        else:
            return None

    def retrieve_audience(self, obj):
        try:
            aud = Audience_xref.objects.get(p_key=obj.placement_id)
            return Audience.objects.get(audience_key=aud.a_key)
        except:
            return False

    def get_audience_key(self, obj):
        aud = self.retrieve_audience(obj)
        if aud:
            return aud.audience_key
        else:
            return None

    def get_audience_description(self, obj):
        aud = self.retrieve_audience(obj)
        if aud:
            return aud.audience_description
        else:
            return None

    def get_audience_created_on(self, obj):
        aud = self.retrieve_audience(obj)
        if aud:
            return aud.created_on
        else:
            return None

    def get_audience_updated_on(self, obj):
        aud = self.retrieve_audience(obj)
        if aud:
            return aud.updated
        else:
            return None

    def retrieve_intent(self, obj):
        try:
            intent = Intent_xref.objects.get(p_key=obj.placement_id)
            return Intent.objects.get(intent_key=intent.i_key)
        except:
            return False

    def get_intent_key(self, obj):
        intent = self.retrieve_intent(obj)
        if intent:
            return intent.intent_key
        else:
            return None

    def get_intent_description(self, obj):
        intent = self.retrieve_intent(obj)
        if intent:
            return intent.intent_description
        else:
            return None

    def get_intent_created_on(self, obj):
        intent = self.retrieve_intent(obj)
        if intent:
            return intent.created_on
        else:
            return None

    def get_intent_updated_on(self, obj):
        intent = self.retrieve_intent(obj)
        if intent:
            return intent.updated
        else:
            return None

    def retrieve_lifecycle(self, obj):
        try:
            lc = Lifecycle_xref.objects.get(p_key=obj.placement_id)
            return LifeCycle.objects.get(lifecycle_key=lc.lc_key)
        except:
            return False

    def get_lifecycle_key(self, obj):
        lc = self.retrieve_lifecycle(obj)
        if lc:
            return lc.lifecycle_key
        else:
            return None

    def get_lifecycle_description(self, obj):
        lc = self.retrieve_lifecycle(obj)
        if lc:
            return lc.lifecycle_description
        else:
            return None

    def get_lifecycle_created_on(self, obj):
        lc = self.retrieve_lifecycle(obj)
        if lc:
            return lc.created_on
        else:
            return None

    def get_lifecycle_updated_on(self, obj):
        lc = self.retrieve_lifecycle(obj)
        if lc:
            return lc.updated
        else:
            return None

    def retrieve_lob(self, obj):
        try:
            lob = LOB_xref.objects.get(p_key=obj.placement_id)
            return LOB.objects.get(lob_key=lob.lob_key)
        except:
            return False

    def get_lob_key(self, obj):
        lob = self.retrieve_lob(obj)
        if lob:
            return lob.lob_key
        else:
            return None

    def get_lob_description(self, obj):
        lob = self.retrieve_lob(obj)
        if lob:
            return lob.lob_description
        else:
            return None

    def get_lob_created_on(self, obj):
        lob = self.retrieve_lob(obj)
        if lob:
            return lob.created_on
        else:
            return None

    def get_lob_updated_on(self, obj):
        lob = self.retrieve_lob(obj)
        if lob:
            return lob.updated
        else:
            return None
