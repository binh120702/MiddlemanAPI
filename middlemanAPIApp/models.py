from django.db import models
from django.db.models.fields import FloatField

# Create your models here.

class TextToSpeechRequest(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=2000)
    voice_type = models.CharField(max_length=255)
    voice_speed = models.CharField(max_length=255)
    voice_url = models.CharField(max_length=255)
    class Meta:
        ordering = ['created']  