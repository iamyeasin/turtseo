from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
# from . models import 
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def add_data(request):
	print("request aise")
	# if request.method == 'POST':
	# 	linkid = request.POST['linkid']
	# 	exampleFormControlFile1 = request.POST['exampleFormControlFile1']
	# 	tagarea = request.POST['tagarea']
	# 	niche = request.POST['niche']
	# 	dr = request.POST['dr']
	# 	da = request.POST['da']
	# 	spamscore = request.POST['spamscore']
	# 	traffic = request.POST['traffic']
	# 	existingcost = request.POST['existingcost']
	# 	newCost = request.POST['new Cost']
	# 	email = request.POST['email']		

	# return HttpResponse("Data Entry")
	return render(request, 'html/index.html')