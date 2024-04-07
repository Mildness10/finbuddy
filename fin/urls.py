from .views import HomePageView, LearnPageView
from django.urls import path

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('learn/', LearnPageView.as_view(), name='learn'),
]