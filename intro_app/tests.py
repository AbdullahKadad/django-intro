from django.test import TestCase, SimpleTestCase
from django.urls import reverse

# Create your tests here.

class TestHomePage(SimpleTestCase):
    def test_status(self):
        url = reverse('HTML')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_template_used(self):
        url = reverse('HTML')
        res = self.client.get(url)
        self.assertTemplateUsed(res, 'home.html')

class TestCascadingStyleSheetsPage(SimpleTestCase):
    def test_status(self):
        url = reverse('CascadingStyleSheets')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_template_used(self):
        url = reverse('CascadingStyleSheets')
        res = self.client.get(url)
        self.assertTemplateUsed(res, 'css.html')

class TestJavaScriptPage(SimpleTestCase):
    def test_status(self):
        url = reverse('JavaScript')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_template_used(self):
        url = reverse('JavaScript')
        res = self.client.get(url)
        self.assertTemplateUsed(res, 'js.html')