from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import requests
from decouple import config

from django.contrib.auth.models import User
from weather.serializers import GetInfo

class Home(APIView):
    permission_classes = (AllowAny,)
    def post(self,request,*args,**kwargs):
        api_key = config('api_key')
        serializer = GetInfo(data = request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            api_url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={name}"
            response = requests.get(api_url)
            data = response.json()
            context = {
                'data':data
            }
            return Response(context)
        return Response('not good')
