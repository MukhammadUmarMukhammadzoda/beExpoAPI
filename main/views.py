from pyexpat import model
from django.http import HttpResponse
from django.shortcuts import render
from .serializers import *
from rest_framework import generics,permissions
from .models import *


# Create your views here.
class Ari(generics.ListCreateAPIView):
    queryset = Ari.objects.all()
    serializer_class = AriSerializer


class Asal(generics.ListAPIView):
    queryset = Asal.objects.all()
    serializer_class = AsalSerializer



class Company(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer



class Klient(generics.ListCreateAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer

class Comment(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


    