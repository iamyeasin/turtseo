from django.urls import path
from . import views

urlpatterns = [
    path('', views.FileUpload, name = 'index'), #hit from "Home" page
    path('search', views.Search, name = 'search'), #hit from "Search" page
    path('url_list', views.Search_Url_list, name = 'url_list'), #hit from "Show URL" button in "Search" page
    path('directory', views.Directory, name = 'directory'), #hit from "Directory" page
]