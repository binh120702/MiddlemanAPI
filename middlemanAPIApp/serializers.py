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
    voice_url = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return TextToSpeechRequest.objects.create(validated_data)
    
    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.voice_type = validated_data.get('voice_type', instance.voice_type)
        instance.voice_speed = validated_data.get('voice_speed', instance.voice_speed)
        instance.voice_url = validated_data.get('voice_url', instance.voice_url)
        instance.save()
        return instance