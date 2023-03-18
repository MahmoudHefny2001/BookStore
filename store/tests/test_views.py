from importlib import import_module
from unittest import skip

from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from store.models import Category, Product
from store.views import product_all


@skip("demonstrating skipping")
class TestSkip(TestCase):
    def test_skip_example(self):
        pass


    def test_homepage_url(self):
        """
        Test homepage response status
        """
        response = self.Client.get('/')


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='Hefny')
        Product.objects.create(
            category_id = 1,
            created_by_id = 1,
            title = 'django beginners',
            image = 'django',
            slug = 'django-beginners',
            price = '20.00',
        )


    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    
    def test_product_detail_url(self):
        """
        Test product response status
        """
        response = self.c.get(reverse('store:product_detail', args=['django-beginners']))
        self.assertEqual(response.status_code, 200)

    
    def test_category_detail_url(self):
        """
        Test Category response status
        """
        response = self.c.get(reverse('store:category_list', args=['django']))
        self.assertEqual(response.status_code, 200)

    
    def test_home_page_html(self):
        request = HttpRequest()
        engine = import_module(settings.SESSION_ENGINE)
        request.session = engine.SessionStore()
        response = product_all(request)
        html = response.content.decode('utf8')
        # print(html)
        self.assertIn('<title>BookStore</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)


    def test_view_function(self):
        request = self.factory.get('/django-beginners')
        response = product_all(request)
        html = response.content.decode('utf8')
        # print(html)
        self.assertIn('<title>BookStore</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)


    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        """
        response = self.c.get('/', HTTP_HOST='noaddress.com')
        self.assertEqual(response.status_code, 400)
        response = self.c.get('/', HTTP_HOST='yourdomain.com')
        self.assertEqual(response.status_code, 200)


    def test_homepage_url(self):
        """
        Test homepage response status
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)