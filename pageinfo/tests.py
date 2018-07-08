from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework import status
from django.urls import reverse


class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="anonymous")
        
        # Initialize client and force it to use authentication
        self.client = APIClient()
        self.client.force_authenticate(user=user)
        
        # Since user model instance is not serializable, use its Id/PK
        self.query_data = {'url': 'http://CNN.com' }
        self.response = self.client.post( '/pageinfo/', self.query_data, format="json")

    def print_response(self):
        """
        Dumps fields of response for debugging purposes
        """
        print( "URL  : ", self.response.data['url'] )
        print( "Title: ", self.response.data['title'] )
        print( "Desc : ", self.response.data['desc'] )
        print( "Tags : ", self.response.data['keywords'] )

    def test_api_can_obtain_info(self):
        """Test the api can obtain page info."""
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_api_part2(self):
        """Test that default values don't prevent return of obtained information."""
        self.query_data = {'url': 'https://CNN.com', 'title':'TheDefaultTitle', 'desc':'Some default description','keywords':'' }
        self.response = self.client.post( '/pageinfo/', self.query_data, format="json")
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_api_get_plain(self):
        """Test GET request withOUT url parameter."""
        self.response = self.client.get( '/pageinfo/', format="json")
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        #self.print_response()

    def test_api_get(self):
        """Test GET request with url parameter and with emoji in response."""
        self.response = self.client.get( '/pageinfo/?url=https://dev.to/oktadev/tutorial-build-a-basic-crud-app-with-nodejs-1ohn', format="json")
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.print_response()

