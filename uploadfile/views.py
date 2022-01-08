from django.http import response
from django.shortcuts import render
from uploadfile.models import Profile
from rest_framework.views import APIView
from rest_framework.response import Response

from uploadfile.serializer import profileSerializer

class ProfilesAPIView(APIView):
    def post(self,request):
        serializer = profileSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def get(self,request):
        data = Profile.objects.all()
        serializer = profileSerializer(data,many=True)
        return Response(serializer.data)
    
