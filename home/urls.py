from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index,name="home"),
    path("open",views.open , name="open"),
    path("upload",views.upload , name="upload")
]

