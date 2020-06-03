from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
# from . models import 
from django.views.decorators.csrf import csrf_exempt

import csv

@csrf_exempt
def FileUpload(request):
	print("File Upload")
	
	if request.method == "POST":
		exelFile = request.FILES.get('file')
		fileName = str(exelFile)
		print(fileName)

	# return HttpResponse("OK")
	return render(request, 'html/index.html')

