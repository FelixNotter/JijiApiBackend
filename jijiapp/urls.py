
from django.contrib import admin
from django.urls import path,include
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView 


urlpatterns = [
    path('api_schema',get_schema_view(title= 'API schema',description='Guide for the REST API'), name='api_schema'),
    path('admin/', admin.site.urls),
    path('jiji/', include('jiji.urls')),
   
]
