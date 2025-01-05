from django.shortcuts import render
from . import models 
# from django.http import HttpResponse
# from django.http import JsonResponse
from rest_framework.views  import APIView
from rest_framework.response import Response
from .serializer import *
# Create your views here.

class Documents(APIView):
    def get(self, request):
        documents = Document.objects.all()
        serializer = ReactSerializer(documents, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    # def delete(self, request):
    #     document = Document.objects.get(id=request.data['id'])
    #     document.delete()
    #     return Response(status=204)
    
    # def put(self, request):
    #     document = Document.objects.get(id=request.data['id'])
    #     serializer = ReactSerializer(document, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=400)