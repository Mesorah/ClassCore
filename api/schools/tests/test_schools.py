from django.urls import reverse
from rest_framework.test import APITestCase


class TestSchools(APITestCase):
    def setUp(self):
        self.name = 'CEMEC'
        self.address = 'cambará'

        return super().setUp()

    def test_school_returns_status_200(self):
        response = self.client.get(reverse('schools:list'))

        self.assertEqual(response.status_code, 200)

    def test_school_returns_status_201(self):
        response = self.client.post(reverse('schools:list'), {
            'name': self.name,
            'address': self.address
        })

        self.assertEqual(response.status_code, 201)
