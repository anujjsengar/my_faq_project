# my_faq_app/views.py
from rest_framework import viewsets
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer
from django.http import HttpResponse
class FAQViewSet(viewsets.ViewSet):
    
    def list(self, request):
        lang = request.GET.get('lang', 'en')  
        faqs = FAQ.objects.all()  
        data = []

    
        for faq in faqs:
            data.append({
                'question': faq.get_translated_question(lang),  
                'answer': faq.answer, 
            })

        return Response(data)