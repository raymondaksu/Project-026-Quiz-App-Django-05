from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from. serializers import RegistrationSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
