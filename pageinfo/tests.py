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
        
        print( 'Create path : ', reverse('create') )
        # Since user model instance is not serializable, use its Id/PK
        self.query_data = {'url': 'http://CNN.com' }
        self.response = self.client.post( reverse('create'), self.query_data, format="json")

    def test_api_can_obtain_info(self):
        """Test the api can obtain page info."""
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        print( "URL  : ", self.response.data['url'] )
        print( "Title: ", self.response.data['title'] )
        print( "Desc : ", self.response.data['desc'] )
