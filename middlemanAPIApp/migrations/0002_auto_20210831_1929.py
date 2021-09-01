# Generated by Django 3.2.6 on 2021-08-31 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('middlemanAPIApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextToSpeechRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('text', models.CharField(max_length=2000)),
                ('voice_type', models.CharField(max_length=255)),
                ('voice_speed', models.CharField(max_length=255)),
                ('voice_url', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.DeleteModel(
            name='TextToSpeech',
        ),
    ]