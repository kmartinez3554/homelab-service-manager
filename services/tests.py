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

class ServiceCreateTests(TestCase):

    """Verifies that the service create page loads properly """
    def test_service_create_page_loads(self):

        response = self.client.get(
            reverse('services:service_create')
        )
    
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'services/service_form.html')

    """ Verifies that service create acutally creates a service """
    def test_valid_form_creates_service(self):

        response = self.client.post(
            reverse('services:service_create'),{
                'name': 'Test',
                'description': 'Test description',
                'host': 'localhost',
                'port': 1111,
                'url': 'http://localhost:1111',
                'service_type': 'Test',
                'is_active': 'on',
            }
        )

        self.assertTrue(Service.objects.filter(name = 'Test').exists())
        self.assertTrue(Service.objects.filter(description = 'Test description').exists())
        self.assertTrue(Service.objects.filter(host = 'localhost').exists())
        self.assertTrue(Service.objects.filter(port = 1111).exists())
        self.assertTrue(Service.objects.filter(url = 'http://localhost:1111').exists())
        self.assertTrue(Service.objects.filter(service_type = 'Test').exists())

        self.assertRedirects(response, reverse('services:service_list'))

    """ Verifies that invalid submissions are not created """
    def test_invalid_form_does_not_create_service(self):

        response = self.client.post(
            reverse('services:service_create'),{
                'name': 'Test',
                'description': 'Test description',
                'host': 'localhost',
                'port': -1,
                'url': 'http://localhost:0000',
                'service_type': 'Test',
                'is_active': 'on',
            }
        )

        self.assertEqual(response.status_code, 200)

        self.assertFalse(Service.objects.filter(name = 'Test').exists())

        self.assertIn('port', response.context['form'].errors)

