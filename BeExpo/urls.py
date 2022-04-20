from django.contrib import admin
from django.urls import path,include
from rest_framework.schemas import get_schema_view # new
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions




schema_view = get_schema_view( # new
openapi.Info(
title="Blog API",
default_version="v1",
description="A sample API for learning DRF",
terms_of_service="https://www.google.com/policies/terms/",
contact=openapi.Contact(email="hello@example.com"),
license=openapi.License(name="BSD License"),
),
public=True,
permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
   path('', include('main.urls')),

path('swagger/', schema_view.with_ui( 
'swagger', cache_timeout=0), name='schema-swagger-ui'),
path('redoc/', schema_view.with_ui( 
'redoc', cache_timeout=0), name='schema-redoc'),

]
