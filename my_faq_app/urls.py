from django.urls import path
from .views import FAQViewSet 

urlpatterns = [
    path('faqs/', FAQViewSet.as_view({'get': 'list'}), name='faq-list'),
]