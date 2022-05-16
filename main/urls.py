from django.urls import path
from . import views

urlpatterns = [
    path('',views.Arii.as_view()),
    path('asal', views.Asall.as_view()),
    path('klient', views.Klient.as_view()),
    path('company', views.Company.as_view()),
    path('asal/<int:pk>', views.Asaldetail.as_view()),
    path('ari/<int:pk>', views.Aridetail.as_view()),
    path('ingradient/', views.IngradientView.as_view()),
    path('ingradient/<int:pk>/', views.Ingradientdetail.as_view()),
    path('contact', views.contactform, name='contact')




    
    
    ]