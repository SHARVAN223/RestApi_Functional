from rest_framework import serializers
from app.models import *

class Stu1_serializer(serializers.ModelSerializer):
    class Meta:
        model = Student1
        fields = '__all__'
    