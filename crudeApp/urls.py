"""
URL configuration for crudeapplication project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from .import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.index),
    path('edd',v.eddemp),
    path('delete/<int:pk>',v.delete.as_view()),
    path('edit/<int:eid>',v.edit),
    path('list',v.emplist),
    path('imgl',v.imglist),
    path('car',v.empimg),
    path('delete2/<int:pk>',v.delete_img.as_view()),
    path('edit_img/<int:eid>',v.edit_img),
]
