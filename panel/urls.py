from django.urls import path
from . import views

urlpatterns = [
    path('', views.FileUpload, name = 'index'),
    path('search',views.Search, name = 'search'),
]