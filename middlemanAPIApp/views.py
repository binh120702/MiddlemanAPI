from re import S
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TextToSpeechRequest
from .serializers import RequestSerializer, GetAllRequestsSerializer
from rest_framework import permissions
import os
from dotenv import load_dotenv
import requests
import json
load_dotenv()
# Create your views here.

def     get_voice_url(input):
    headers = {
        'apikey': os.getenv('API_KEY'),
    }
    print(input.data['text'])
    data = {
        'speaker_id': input.data['voice_type'],
        'speed': input.data['voice_speed'],
        'input': input.data['text']
    }
    response = requests.post('https://api.zalo.ai/v1/tts/synthesize',headers=headers,data=data)
    json_object = json.loads(response.text)
    return json_object["data"]["url"]
    

class   getAllRequestAPIView(APIView):

    def get(self, request):
        request_list = TextToSpeechRequest.objects.all()
        response_data = GetAllRequestsSerializer(request_list, many=True)
        return Response(data = response_data.data, status=status.HTTP_200_OK)
    permission_classes = [permissions.IsAuthenticated]

class TextToSpeechAPIView(APIView):
    def post(self, request):
        new_data = RequestSerializer(data=request.data)
        if not new_data.is_valid():
            return Response(new_data.errors, status=status.HTTP_400_BAD_REQUEST)
        zalo_voice_url = get_voice_url(new_data)
        TextToSpeechRequest.objects.create(text = new_data.data['text'], voice_type = new_data.data['voice_type'], voice_speed = new_data.data['voice_speed'], voice_url = zalo_voice_url)
        return Response(zalo_voice_url, status = status.HTTP_200_OK)