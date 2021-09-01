from re import S
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TextToSpeechRequest
from .serializers import RequestSerializer, GetAllRequestsSerializer

# Create your views here.

class   getSpeechAPIView(APIView):

    def get(self, request):
        request_list = TextToSpeechRequest.objects.all()
        response_data = GetAllRequestsSerializer(request_list, many=True)
        return Response(data = response_data.data, status=status.HTTP_200_OK)

    def post(self, request):
        new_data = RequestSerializer(data=request.data)
        if not new_data.is_valid():
            return Response(new_data.errors, status=status.HTTP_400_BAD_REQUEST)
        
        temp = TextToSpeechRequest.objects.create(text = new_data.data['text'])
        return Response(temp.id, status = status.HTTP_200_OK)