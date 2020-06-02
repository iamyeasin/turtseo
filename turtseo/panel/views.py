from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
# from . models import 
# from django.views.decorators.csrf import csrf_exempt


# @csrf_exempt
def add_data(request):
	return HttpResponse("Data Entry")