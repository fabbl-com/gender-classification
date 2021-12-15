from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# User Serializer
class ClassifierSerializer(serializers.Serializer):
    audio = serializers.FileField()

