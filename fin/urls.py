from .views import HomePageView, LearnPageView, FeedbackPageView, FinHealthPageView, FinAdvisorPageView
from django.urls import path

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('learn/', LearnPageView.as_view(), name='learn'),
    path('feedback/', FeedbackPageView.as_view(), name='feedback'),
    path('finhealth/', FinHealthPageView.as_view(), name='finhealth'),
    path('finadvisor/', FinAdvisorPageView.as_view(), name='finadvisor'),
]