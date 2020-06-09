from django.urls import path
from . import views

urlpatterns = [
    path('', views.FileUpload, name = 'index'),
    path('search', views.Search, name = 'search'),
    path('url_list', views.Search_Url_list, name = 'url_list'),
]