from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from .advisor import get_advisor_response
import logging
import json

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class LearnPageView(TemplateView):
    template_name = 'learn.html'

class FeedbackPageView(TemplateView):
    template_name = 'feedback.html'

class FinHealthPageView(TemplateView):
    template_name = 'finhealth.html'

class FinAdvisorPageView(TemplateView):
    template_name = 'finadvisor.html'
    
    def post(self, request, *args, **kwargs):
            try:
                data = json.loads(request.body.decode('utf-8'))
                user_message = data.get('userMessage', '')  

                advisor_response = get_advisor_response(user_message)
                
                return JsonResponse({'response': advisor_response})
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON data'}, status=400)