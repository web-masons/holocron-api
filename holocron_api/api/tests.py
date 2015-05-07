from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Source, Medium, Campaign, Content, Placement


class SourceTest(APITestCase):
    def create_test(self, source_name="Test Source"):
        return Source.objects.create(source_name=source_name)

    def test_was_created(self):
        s = self.create_test()
        self.assertTrue(isinstance(s, Source))


class MediumTest(APITestCase):
    def create_test(self, medium_name="Test Medium"):
        return Medium.objects.create(medium_name=medium_name)

    def test_was_created(self):
        m = self.create_test()
        self.assertTrue(isinstance(m, Medium))

class ContentTest(APITestCase):
    def create_test(self, content_name="Test Content", content_description="I am a piece of Content!"):
        return Content.objects.create(content_name=content_name, content_description=content_description)

    def test_was_created(self):
        co = self.create_test()
        self.assertTrue(isinstance(co, Content))

class CampaignTest(APITestCase):
    def create_test(self, campaign_name="Test Campaign", campaign_description="I am a test Campaign", end_date="2020-09-20"):
        return Campaign.objects.create(campaign_name=campaign_name, campaign_description=campaign_description, end_date=end_date)

    def test_was_created(self):
        ca = self.create_test()
        self.assertTrue(isinstance(ca, Campaign))

class PlacementTest(APITestCase):
    def create_campaign_test(self, campaign_name="Test Campaign", campaign_description="I am a test Campaign", end_date="2020-09-20"):
        return Campaign.objects.create(campaign_name=campaign_name, campaign_description=campaign_description, end_date=end_date)

    def create_medium_test(self, medium_name="Test Medium"):
        return Medium.objects.create(medium_name=medium_name)

    def create_source_test(self, source_name="Test Source"):
        return Source.objects.create(source_name=source_name)

    def create_content_test(self, content_name="Test Content", content_description="I am a piece of Content!"):
        return Content.objects.create(content_name=content_name, content_description=content_description)

    def create_test(self, placement_name="Test Placement", end_date="2020-09-20"):
        ca = self.create_campaign_test()
        m = self.create_medium_test()
        s = self.create_source_test()
        co = self.create_content_test()
        return Placement.objects.create(placement_name=placement_name, end_date=end_date, campaign=ca, medium=m, source=s, content=co)

    def test_was_created(self):
        p = self.create_test()
        self.assertTrue(isinstance(p, Placement))

