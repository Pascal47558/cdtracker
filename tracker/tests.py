from django.test import TestCase, Client
from django.urls import reverse

from .models import CD

# Create your tests here.
class WebRequestTest(TestCase):
    def setUp(self):
        self.client = Client

    def testMainPage(self):
        # Should uncoment this
        #response = self.client.get(reverse('index'))

        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "CD Tracker!")

        self.assertTemplateUsed(response, "index.html")

    def test_pageNotFound(self):
        response = self.client.get("/notarealpage")

        self.assertEqual(response.status_code, 404)
        self.assertContains(response, "404")
        self.assertContains(response, "Page Not Found")
        self.assertTemplateUsed(response, "404.html")

    def test_itemNotFound(self):
        response = self.client.get("cd/13241322134")

        self.assertEqual(response.status_code, 404)
        self.assertContains(response, "404")
        self.assertContains(response, "Page Not Found")
        self.assertTemplateNotUsed(response, "detail.html")
        self.assertTemplateUsed(response, "404.html")