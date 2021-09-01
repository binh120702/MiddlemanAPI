from django.urls import path
from middlemanAPIApp import views

urlpatterns = [
    path('requestlist/', views.getSpeechAPIView.as_view())
]