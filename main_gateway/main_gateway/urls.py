"""
URL configuration for main_gateway project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import path


def index(request):
    return render(request, "index.html")

def redirect_to_server(request, server_url):
    return HttpResponseRedirect(server_url)

urlpatterns = [
    path('', index, name='home'),
    path('server2/', lambda request: redirect_to_server(request, 'http://localhost:8001/')),
    path('server3/', lambda request: redirect_to_server(request, 'http://localhost:8002/')),
    path('server4/', lambda request: redirect_to_server(request, 'http://localhost:8003/')),
]
