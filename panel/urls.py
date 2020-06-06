from django.urls import path
from . import views

urlpatterns = [
    path('', views.FileUpload, name = ''),
    path('search',views.Search, name = 'search'),
]