from django.http import HttpResponse
from django.shortcuts import render
from requests import Response
from .serializers import *
from rest_framework import generics,permissions
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.decorators import api_view

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


@api_view(['post'])
def SendEmailView(request):
    email_admin = 'mukhmmadzodamukhammadumar@gmail.com'
    user_email = request.POST['email']
    name = request.POST['name']
    subject = request.POST['subject']
    message = request.POST['message']
    send_mail(
        f'{subject} from {user_email}  '
        
        ,
         f'{message}',

                      settings.DEFAULT_FROM_EMAIL, [email_admin])
    return Response([])