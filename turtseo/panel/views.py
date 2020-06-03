from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
# from . models import 
from django.views.decorators.csrf import csrf_exempt

import json

@csrf_exempt
def FileUpload(request):
	print("File Upload")
	
	if request.method == 'POST':
		file = json.loads(request.POST.get('sample'))
		print(file)
		print(str(file))
	else:
		print("Fuck")
	
	return render(request, 'html/index.html')

