from django.urls import path
from . import views

urlpatterns = [    
    path('add_data',views.add_data, name = 'add_data'),    
]