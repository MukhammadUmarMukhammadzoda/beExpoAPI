from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
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


@api_view(['POST'])
def SendEmailView(request):
    try:
        email_admin = 'mukhammadzodamukhammadumar@gmail.com'
        user_email = request.data['email']
        name = request.data['name']
        subject = request.data['subject']
        message = request.data['message']
        send_mail(
            f'{subject} from {user_email}  '
            
            ,
            f'{message}',

                        settings.DEFAULT_FROM_EMAIL, [email_admin])
        data = {
            "success":True,
            "data":{}
        }
    except Exception as err:
        data = {
            "success":False,
            "error":f"{err}"
        }

    return Response(data)