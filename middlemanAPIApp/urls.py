from django.urls import path
from middlemanAPIApp import views

urlpatterns = [
    path('requestlist/', views.getAllRequestAPIView.as_view()),
    path('addrequest/', views.TextToSpeechAPIView.as_view())
]