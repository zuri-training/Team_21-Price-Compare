"""priceBetaProject URL Configuration

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
import django.contrib.auth.views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from priceBetaApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("Accounts.urls")),
    path("", include("priceBetaApp.urls")),
]



# Configuring the media folder 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings    )
