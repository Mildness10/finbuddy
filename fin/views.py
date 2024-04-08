from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class LearnPageView(TemplateView):
    template_name = 'learn.html'

class FeedbackPageView(TemplateView):
    template_name = 'feedback.html'

class FinHealthPageView(TemplateView):
    template_name = 'finhealth.html'