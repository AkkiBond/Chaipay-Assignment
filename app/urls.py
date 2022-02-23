"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path as url
from app.api.views import capture_charge, create_charge, list_charges, create_refund

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/v1/create_charge',create_charge),
    url(r'^api/v1/capture_charge/(?P<pid>[\w-]+)',capture_charge),
    url(r'^api/v1/get_charges',list_charges),
    url(r'^api/v1/create_refund/(?P<pid>[\w-]+)',create_refund)
]
