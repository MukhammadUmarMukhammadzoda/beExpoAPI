from django.urls import path
from . import views

urlpatterns = [
    path('',views.Ari.as_view()),
    path('asal', views.Asal.as_view()),
    path('klient', views.Klient.as_view()),
    path('company', views.Company.as_view()),
    path('comment', views.Comment.as_view()),


    
    
    ]