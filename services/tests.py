from django.test import TestCase
from django.urls import reverse

from .models import Service

class ServiceListTests(TestCase):

    """ Verifies that the service list page loads """
    def test_service_list_page_loads(self):

        response = self.client.get(
            reverse('services:service_list')
        )

        self.assertEqual(response.status_code, 200)

    """ Verifies that the correct service populates on service list page """
    def test_service_list_populates_correctly(self):

        Service.objects.create(
            name = 'Jellyfin',
            description = 'Media streaming server',
            host = 'localhost',
            port = 8096,
            service_type = 'Media',
        )

        response = self.client.get(
            reverse('services:service_list')
        )

        self.assertContains(response, 'Jellyfin')
