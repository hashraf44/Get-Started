from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User


class taskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        field = '__all__'

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = ['id', 'username', 'email']
