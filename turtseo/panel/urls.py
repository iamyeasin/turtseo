from django.urls import path
from . import views

urlpatterns = [
    path('', views.FileUpload, name = ''),
    # path('add_data',views.add_data, name = 'add_data'),
    path('search',views.search, name = 'search'),
]