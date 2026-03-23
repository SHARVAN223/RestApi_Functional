from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from app.models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def student(req):
    if req.method == 'POST':
        serializer = Stu1_serializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    data = Student1.objects.all()
    serializer = Stu1_serializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET','PUT','PATCH','DELETE'])
def student1(req,pk):
    user=Student1.objects.filter(id=pk)
    if user:
        if req.method == 'PUT':
            data = Student1.objects.get(pk=pk)
            serializer = Stu1_serializer(data, data=req.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif req.method == 'PATCH':
            data = Student1.objects.get(pk=pk)
            serializer = Stu1_serializer(data, data=req.data , partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif req.method == 'DELETE':
            data = Student1.objects.get(pk=pk)
            data.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif req.method == 'GET':
            data = Student1.objects.all()
            serializer = Stu1_serializer(data, many=True)
            return Response(serializer.data)
    return JsonResponse({'msg':'id is not db'},content_type='application/json')
    
    


    

