# my_faq_app/tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import FAQ

class FAQAPITests(APITestCase):
    def setUp(self):
        # Create some FAQs for testing
        self.faq1 = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a high-level Python web framework.",
            question_hi="डjango क्या है?",
            question_bn="ডjango কি?"
        )
        self.faq2 = FAQ.objects.create(
            question="What is REST?",
            answer="REST stands for Representational State Transfer.",
            question_hi="REST क्या है?",
            question_bn="REST কি?"
        )

    def test_fetch_faqs_default_language(self):
        """Test fetching FAQs in English (default)"""
        response = self.client.get(reverse('faq-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # We created 2 FAQs
        self.assertEqual(response.data[0]['question'], "What is Django?")

    def test_fetch_faqs_hindi(self):
        """Test fetching FAQs in Hindi"""
        response = self.client.get(reverse('faq-list'), {'lang': 'hi'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['question'], "डjango क्या है?")

    def test_fetch_faqs_bengali(self):
        """Test fetching FAQs in Bengali"""
        response = self.client.get(reverse('faq-list'), {'lang': 'bn'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['question'], "ডjango কি?")

    def test_faq_creation(self):
        """Test creating a new FAQ"""
        data = {
            'question': "What is Python?",
            'answer': "Python is a programming language.",
            'question_hi': "Python क्या है?",
            'question_bn': "Python কি?"
        }
        response = self.client.post(reverse('faq-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(FAQ.objects.count(), 3)  # We should have 3 FAQs now