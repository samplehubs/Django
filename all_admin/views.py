from django.shortcuts import render

# Create your views here.
from urllib import response
from django.shortcuts import render
from rest_framework.generics import GenericAPIView

from list.settings import JWT_SECRET_KEY
from .serializers import *
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from datetime import datetime, timedelta
import jwt
from django.conf import settings



#Register API
class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def get(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')
        user = authenticate(username=username, password=password)

        if user:
            auth_token = jwt.encode(
                {'username': user.username, 'exp': datetime.utcnow() + timedelta(hours=8)}, str(settings.JWT_SECRET_KEY), algorithm="HS256")

            serializer = self.serializer_class(user)
        
            data = {'token': auth_token}
           
            return Response(data, status=status.HTTP_200_OK)

            # SEND RES
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(GenericAPIView):
    def delete(self, request):
        token = request.data.get('http://192.168.0.102:8000/allitson/admin/login')
        print(token)
        response = RefreshToken(JWT_SECRET_KEY)
        response.blacklist()
        return Response({'message': 'success'}, status=status.HTTP_200_OK)