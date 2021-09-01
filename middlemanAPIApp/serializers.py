from rest_framework import serializers
from .models import TextToSpeechRequest

class GetAllRequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextToSpeechRequest
        fields = ['id','created','text','voice_type','voice_speed','voice_url']

class RequestSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=255)
    voice_type = serializers.CharField(max_length=255)
    voice_speed = serializers.CharField(max_length=255)
