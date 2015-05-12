from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.test import TestCase
from api.models import Source, Medium, Campaign, Content, Placement
from rest_framework import status
import factory


class SourceFactory(factory.DjangoModelFactory):
    class Meta:
        model = Source
    source_name = "Testing Source"
    source_id = 1


class MediumFactory(factory.DjangoModelFactory):
    class Meta:
        model = Medium
    medium_name = "Testing Medium"
    medium_id = 1


class CampaignFactory(factory.DjangoModelFactory):
    class Meta:
        model = Campaign
    campaign_name = "Testing Campaign"
    campaign_description = "This is a Test"
    end_date = "2040-12-12"
    campaign_id = 1


class ContentFactory(factory.DjangoModelFactory):
    class Meta:
        model = Content
    content_name = "Testing Content"
    content_description = "This is a test for Content"
    content_id = 1


class SourceTest(APITestCase):

    @staticmethod
    def create_test(source_name="Test Source"):
        return Source.objects.create(source_name=source_name)

    def test_was_created(self):
        s = self.create_test()
        self.assertTrue(isinstance(s, Source))


class MediumTest(APITestCase):

    @staticmethod
    def create_test(medium_name="Test Medium"):
        return Medium.objects.create(medium_name=medium_name)

    def test_was_created(self):
        m = self.create_test()
        self.assertTrue(isinstance(m, Medium))


class ContentTest(APITestCase):

    @staticmethod
    def create_test(content_name="Test Content",
                    content_description="I am a piece of Content!"):
        return Content.objects.create(content_name=content_name,
                                      content_description=content_description)

    def test_was_created(self):
        co = self.create_test()
        self.assertTrue(isinstance(co, Content))


class CampaignTest(APITestCase):

    @staticmethod
    def create_test(campaign_name="Test Campaign",
                    campaign_desc="I am a test Campaign",
                    end_date="2020-09-20"):
        return Campaign.objects.create(campaign_name=campaign_name,
                                       campaign_description=campaign_desc,
                                       end_date=end_date)

    def test_was_created(self):
        ca = self.create_test()
        self.assertTrue(isinstance(ca, Campaign))


class PlacementTest(APITestCase):

    @staticmethod
    def create_campaign_test(campaign_name="Test Campaign",
                             campaign_desc="I am a test Campaign",
                             end_date="2020-09-20"):
        return Campaign.objects.create(campaign_name=campaign_name,
                                       campaign_description=campaign_desc,
                                       end_date=end_date)

    @staticmethod
    def create_medium_test(medium_name="Test Medium"):
        return Medium.objects.create(medium_name=medium_name)

    @staticmethod
    def create_source_test(source_name="Test Source"):
        return Source.objects.create(source_name=source_name)

    @staticmethod
    def create_content_test(content_name="Test Content",
                            content_description="I am a piece of Content!"):
        return Content.objects.create(content_name=content_name,
                                      content_description=content_description)

    @staticmethod
    def create_test(self, placement_name="Test Placement",
                    end_date="2020-09-20"):
        ca = self.create_campaign_test()
        m = self.create_medium_test()
        s = self.create_source_test()
        co = self.create_content_test()
        return Placement.objects.create(placement_name=placement_name,
                                        end_date=end_date, campaign=ca,
                                        medium=m, source=s, content=co)

    def test_was_created(self):
        p = self.create_test(self)
        self.assertTrue(isinstance(p, Placement))


class SourceAPITest(APITestCase):
    def test_post_source_api(self):
        data = {'source_name': 'My Source'}
        response = self.client.post('/source/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_source_api(self):
        client = APIClient()
        response = client.get("/source/")
        self.assertEqual(response.status_code, 200)

    def test_empty_post_source_api(self):
        data = {'source_name': ''}
        response = self.client.post('/source/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_no_data_post_source_api(self):
        data = {}
        response = self.client.post('/source/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_bad_param_post_source_api(self):
        data = {'name': 'test'}
        response = self.client.post('/source/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_too_long_post_source_api(self):
        data = {'source_name': 'Random o85y9384ytoerty3849yroehg '
                               'yhvytvytoa8y4tyv8ytoeryto8y34o8ythiua48y'
                               'tlai4ytai47tyiow4t8orghowiy4toi4ehtoweit'}
        response = self.client.post('/source/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class MediumAPITest(APITestCase):
    def test_post_medium_api(self):
        data = {'medium_name': 'My Meduim'}
        response = self.client.post('/medium/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_medium_api(self):
        client = APIClient()
        response = client.get("/medium/")
        self.assertEqual(response.status_code, 200)

    def test_empty_post_medium_api(self):
        data = {'medium_name': ''}
        response = self.client.post('/medium/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_no_data_post_medium_api(self):
        data = {}
        response = self.client.post('/medium/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_bad_param_post_medium_api(self):
        data = {'name': 'Test'}
        response = self.client.post('/medium/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_too_long_post_medium_api(self):
        data = {'medium_name': 'Random o85y9384ytoerty3849yroehg '
                               'yhvytvytoa8y4tyv8ytoeryto8y34o8ythiu'
                               'a48ytlai4ytai47tyiow4t8orghowiy4toi4ehtoweit'}
        response = self.client.post('/medium/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class CampaignAPITest(APITestCase):
    def test_post_campaign_api(self):
        data = {'campaign_name': 'My Campaign',
                'campaign_description': 'This one is mine',
                'end_date': '2020-12-12'}
        response = self.client.post('/campaign/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_campaign_api(self):
        client = APIClient()
        response = client.get("/campaign/")
        self.assertEqual(response.status_code, 200)

    def test_empty_name_campaign_api(self):
        data = {'campaign_name': '',
                'campaign_description': 'This one is mine',
                'end_date': '2020-12-12'}
        response = self.client.post('/campaign/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_empty_description_campaign_api(self):
        data = {'campaign_name': 'Test',
                'campaign_description': '',
                'end_date': '2020-12-12'}
        response = self.client.post('/campaign/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_empty_date_campaign_api(self):
        data = {'campaign_name': 'Test',
                'campaign_description': 'This one is mine',
                'end_date': ''}
        response = self.client.post('/campaign/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_missing_name_campaign_api(self):
        data = {'campaign_description': 'This one is mine',
                'end_date': '2020-12-12'}
        response = self.client.post('/campaign/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_missing_description_campaign_api(self):
        data = {'campaign_name': 'Test',
                'end_date': '2020-12-12'}
        response = self.client.post('/campaign/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_missing_date_campaign_api(self):
        data = {'campaign_name': 'Test',
                'campaign_description': 'This one is mine'}
        response = self.client.post('/campaign/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_bad_date_campaign_api(self):
        data = {'campaign_name': 'Test',
                'campaign_description': 'This one is mine',
                'end_date': 'Nov. 2, 2018'}
        response = self.client.post('/campaign/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_no_data_post_campaign_api(self):
        data = {}
        response = self.client.post('/campaign/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_bad_param_post_campaign_api(self):
        data = {'name': 'Test',
                'campaign_description': 'This one is mine',
                'end_date': '2020-12-12'}
        response = self.client.post('/campaign/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_name_too_long_post_campaign_api(self):
        data = {'campaign_name': 'Random o85y9384ytoerty3849yroehg yhvytvyto'
                                 'a8y4tyv8ytoeryto8y34o8ythiua48ytlai4ytai47t'
                                 'yiow4t8orghowiy4toi4ehtoweit',
                'campaign_description': 'This one is mine',
                'end_date': '2020-12-12'}
        response = self.client.post('/campaign/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_description_too_long_post_campaign_api(self):
        data = {'campaign_name': 'Long Description',
                'campaign_description': 'What happens if this is too long '
                                        'srihgoityow aiytowierhtohirgoirytiors'
                                        'hgoheao4yhtoaghrihat;oeirhtahlhghe sf'
                                        'sifghoirhgeoirhgeilrgherigheirfklnvh',
                'end_date': '2020-12-12'}
        response = self.client.post('/campaign/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class ContentAPITest(APITestCase):
    def test_post_content_api(self):
        data = {'content_name': 'My Content',
                'content_description': 'This is my content'}
        response = self.client.post('/content/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_content_api(self):
        client = APIClient()
        response = client.get("/content/")
        self.assertEqual(response.status_code, 200)

    def test_empty_name_content_api(self):
        data = {'content_name': '',
                'content_description': 'This one is mine'}
        response = self.client.post('/content/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_empty_description_content_api(self):
        data = {'content_name': 'Test',
                'content_description': ''}
        response = self.client.post('/content/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_no_data_post_content_api(self):
        data = {}
        response = self.client.post('/content/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_bad_param_post_content_api(self):
        data = {'name': 'Test',
                'content_description': 'This one is mine'}
        response = self.client.post('/content/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_name_too_long_post_content_api(self):
        data = {'content_name': 'Random o85y9384ytoerty3849yroehg '
                                'yhvytvytoa8y4tyv8ytoeryto8y34o8ythi'
                                'ua48ytlai4ytai47tyiow4t8orghowiy4toi4ehto',
                'content_description': 'Name is too long'}
        response = self.client.post('/content/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_description_too_long_post_content_api(self):
        data = {'content_name': 'Description is too long',
                'content_description': 'This is too long. '
                                       'lsirghotyeiyrtoeirhgtoeitoeuto94uti '
                                       'ioeartoeirhto eheoihteoit'
                                       'hoeihtaoeirhteoirhtoei heoirt '
                                       'woirygoeirfhgvoeirshgeoishgsjdfhskjd'}
        response = self.client.post('/content/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class PlacementAPITest(APITestCase):

    @staticmethod
    def make_pks():
        SourceFactory.create()
        MediumFactory.create()
        CampaignFactory.create()
        ContentFactory.create()

    def test_get_placement_api(self):
        client = APIClient()
        response = client.get("/placement/")
        self.assertEqual(response.status_code, 200)

    def test_get_placement_details_api(self):
        client = APIClient()
        response = client.get("/placement-details/")
        self.assertEqual(response.status_code, 200)

    def test_post_placement_api(self):
        self.make_pks()
        data = {"placement_name": "Test Placement",
                "placement_url": "www.testurl.com",
                "end_date": "2040-01-01",
                "campaign": 1,
                "medium": 1,
                "source": 1,
                "content": 1}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_missing_name_placement_api(self):
        self.make_pks()
        data = {"placement_name": "",
                "placement_url": "www.testurl.com",
                "end_date": "2040-01-01",
                "campaign": 1,
                "medium": 1,
                "source": 1,
                "content": 1}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_missing_url_placement_api(self):
        self.make_pks()
        data = {"placement_name": "Test",
                "placement_url": "",
                "end_date": "2040-01-01",
                "campaign": 1,
                "medium": 1,
                "source": 1,
                "content": 1}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_missing_date_placement_api(self):
        self.make_pks()
        data = {"placement_name": "Test",
                "placement_url": "www.testurl.com",
                "end_date": "",
                "campaign": 1,
                "medium": 1,
                "source": 1,
                "content": 1}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_date_placement_api(self):
        self.make_pks()
        data = {"placement_name": "Test",
                "placement_url": "www.testurl.com",
                "end_date": "1-1-2010",
                "campaign": 1,
                "medium": 1,
                "source": 1,
                "content": 1}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_string_date_placement_api(self):
        self.make_pks()
        data = {"placement_name": "Test",
                "placement_url": "www.testurl.com",
                "end_date": "January 1, 2020",
                "campaign": 1,
                "medium": 1,
                "source": 1,
                "content": 1}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_missing_campaign_placement_api(self):
        self.make_pks()
        data = {"placement_name": "Test",
                "placement_url": "www.testurl.com",
                "end_date": "2040-01-01",
                "campaign": "",
                "medium": 1,
                "source": 1,
                "content": 1}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_missing_medium_placement_api(self):
        self.make_pks()
        data = {"placement_name": "Test",
                "placement_url": "www.testurl.com",
                "end_date": "2040-01-01",
                "campaign": 1,
                "medium": "",
                "source": 1,
                "content": 1}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_missing_source_placement_api(self):
        self.make_pks()
        data = {"placement_name": "Test",
                "placement_url": "www.testurl.com",
                "end_date": "2040-01-01",
                "campaign": 1,
                "medium": 1,
                "source": "",
                "content": 1}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_missing_content_placement_api(self):
        self.make_pks()
        data = {"placement_name": "Test",
                "placement_url": "www.testurl.com",
                "end_date": "2040-01-01",
                "campaign": 1,
                "medium": 1,
                "source": 1,
                "content": ""}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_campaign_placement_api(self):
        self.make_pks()
        data = {"placement_name": "Test",
                "placement_url": "www.testurl.com",
                "end_date": "2040-01-01",
                "campaign": 0,
                "medium": 1,
                "source": 1,
                "content": 1}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_medium_placement_api(self):
        self.make_pks()
        data = {"placement_name": "Test",
                "placement_url": "www.testurl.com",
                "end_date": "2040-01-01",
                "campaign": 1,
                "medium": 0,
                "source": 1,
                "content": 1}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_source_placement_api(self):
        self.make_pks()
        data = {"placement_name": "Test",
                "placement_url": "www.testurl.com",
                "end_date": "2040-01-01",
                "campaign": 1,
                "medium": 1,
                "source": 0,
                "content": 1}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_content_placement_api(self):
        self.make_pks()
        data = {"placement_name": "Test",
                "placement_url": "www.testurl.com",
                "end_date": "2040-01-01",
                "campaign": 1,
                "medium": 1,
                "source": 1,
                "content": 0}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_negative_campaign_placement_api(self):
        self.make_pks()
        data = {"placement_name": "Test",
                "placement_url": "www.testurl.com",
                "end_date": "2040-01-01",
                "campaign": -1,
                "medium": 1,
                "source": 1,
                "content": 1}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_negative_medium_placement_api(self):
        self.make_pks()
        data = {"placement_name": "Test",
                "placement_url": "www.testurl.com",
                "end_date": "2040-01-01",
                "campaign": 1,
                "medium": -1,
                "source": 1,
                "content": 1}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_negative_source_placement_api(self):
        self.make_pks()
        data = {"placement_name": "Test",
                "placement_url": "www.testurl.com",
                "end_date": "2040-01-01",
                "campaign": 1,
                "medium": 1,
                "source": -1,
                "content": 1}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_negative_content_placement_api(self):
        self.make_pks()
        data = {"placement_name": "Test",
                "placement_url": "www.testurl.com",
                "end_date": "2040-01-01",
                "campaign": 1,
                "medium": 1,
                "source": 1,
                "content": -1}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_string_campaign_placement_api(self):
        self.make_pks()
        data = {"placement_name": "Test",
                "placement_url": "www.testurl.com",
                "end_date": "2040-01-01",
                "campaign": "One",
                "medium": 1,
                "source": 1,
                "content": 1}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_string_medium_placement_api(self):
        self.make_pks()
        data = {"placement_name": "Test",
                "placement_url": "www.testurl.com",
                "end_date": "2040-01-01",
                "campaign": 1,
                "medium": "Medium",
                "source": 1,
                "content": 1}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_string_source_placement_api(self):
        self.make_pks()
        data = {"placement_name": "Test",
                "placement_url": "www.testurl.com",
                "end_date": "2040-01-01",
                "campaign": 1,
                "medium": 1,
                "source": "Test",
                "content": 1}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_string_content_placement_api(self):
        self.make_pks()
        data = {"placement_name": "Test",
                "placement_url": "www.testurl.com",
                "end_date": "2040-01-01",
                "campaign": 1,
                "medium": 1,
                "source": 1,
                "content": "My Content"}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
