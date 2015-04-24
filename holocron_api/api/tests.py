from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.
class HelloWorldTest(APITestCase):
    def test_hello_world(self):
        """
        Ensure we get back a 200 response code and see Hello World.
        """
        response = self.client.get('')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'message': 'Hello, world!'})

    def test_post(self):
        """
        Ensure we get back a 200 Response and see our posted data.
        """
        data = {'Hello': 'World'}
        response = self.client.post('', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"message": "Got some data!", "data": data})