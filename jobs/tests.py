from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import JobPost

class JobAPITests(TestCase):

    def test_get_job_list(self):
        JobPost.objects.create(
            title="Developer",
            description="Dev job",
            experience="2 years",
            location="NY"
        )
        client = APIClient()
        response = client.get("/api/jobs/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json()) >= 1)

    def test_create_job_authenticated(self):
        user = User.objects.create_user(username="test", password="pass123")
        client = APIClient()
        client.login(username="test", password="pass123")

        data = {
            "title": "Engineer",
            "description": "Testing",
            "experience": "3 years",
            "location": "LA"
        }

        response = client.post("/api/jobs/", data, format='json')
        self.assertEqual(response.status_code, 201)
