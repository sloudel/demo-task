import json
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Page

class PageTests(APITestCase):
    test_title = 'test title'
    def setUp(self):
        Page.objects.create(title=self.test_title)

    def test_index(self):
        response = self.client.get('', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_page_list(self):
        response = self.client.get('/pages/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_page_detail(self):
        response = self.client.get('/pages/', format='json')
        pages = []
        for page in json.loads(response.content):
            page = self.client.get(page['url'], format='json')
            pages.append(json.loads(page.content))
        pages = [page['title'] for page in pages]
        self.assertEqual(self.test_title in pages, True)
    

