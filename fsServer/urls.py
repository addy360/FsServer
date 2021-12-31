from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('dirs',views.directories),
    path('files',views.files),
    path('search',views.search),
]
