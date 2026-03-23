from rest_framework import serializers
from app.models import *

class Stu1_serializer(serializers.Serializer):
    Name = serializers.CharField(max_length=50)
    Email = serializers.EmailField()
    Age = serializers.IntegerField()
    Contact = serializers.CharField(max_length=15)

    def create(self,validated_data):
        return Student1.objects.create(**validated_data)
