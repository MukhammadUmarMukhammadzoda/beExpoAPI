from pyexpat import model
from django.http import HttpResponse
from django.shortcuts import render
from requests import delete
from .serializers import *
from rest_framework import generics,permissions
from .models import *


# Create your views here.
class Arii(generics.ListCreateAPIView):
    queryset = Ari.objects.all()
    serializer_class = AriSerializer

        


class Asall(generics.ListCreateAPIView):
    queryset = Asal.objects.all()
    serializer_class = AsalSerializer



class Company(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer



class Klient(generics.ListCreateAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer


class Asaldetail(generics.RetrieveAPIView):
    queryset = Asal.objects.all()
    serializer_class = AsalSerializer


class Aridetail(generics.RetrieveAPIView):
    queryset = Ari.objects.all()
    serializer_class = AriSerializer


class IngradientView(generics.ListCreateAPIView):
    queryset = Ingradient.objects.all()
    serializer_class = IngradientSerializer


class Ingradientdetail(generics.RetrieveAPIView):
    queryset = Ingradient.objects.all()
    serializer_class = IngradientSerializer


    
