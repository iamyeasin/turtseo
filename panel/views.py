from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404
from . models import *
from . import methods
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

import json

@csrf_exempt
def FileUpload(request):
	if request.method == 'POST':
		post_key_link = request.POST.get('key_link')
		URLList = request.POST.getlist('urlList[]')
		DRList = request.POST.getlist('drList[]')
		post_niche = request.POST.get('niche')
		post_dr = request.POST.get('dr')
		post_da = request.POST.get('da')
		post_spamscore = request.POST.get('spamscore')
		post_traffic = request.POST.get('traffic')
		post_existingcost = request.POST.get('existingcost')
		post_new_Cost = request.POST.get('new_cost')
		post_email = request.POST.get('email')

		isKeyFound = Key_Link_List.objects.filter(key_link = post_key_link).count()

		if(isKeyFound > 0):
			return HttpResponseNotFound('<h1>Duplicate Key Link</h1>')
		else:
			try:
				methods.Model_Key_Link_List_Save(post_key_link)
				methods.Model_Profile_Save(post_key_link, URLList, DRList)
				methods.Model_Link_Counter_Save(post_key_link, URLList)
				methods.Model_Profile_Extended_Save(post_key_link, post_dr, post_da, post_traffic, post_spamscore, post_existingcost, post_new_Cost, post_email, post_niche)
				print("Data Saved")
			except:
				return HttpResponseNotFound("Error in Data Save")
			
	return render(request, 'html/index.html')


@csrf_exempt
def Search(request):
	if request.method == "POST":
		search_key = request.POST.get('search_key')

		# Foreign Key
		link_counter_object = Link_Counter.objects.filter(key_link = search_key)

		serialized = serializers.serialize('json', link_counter_object)

		data = {"dataset": serialized}
		return JsonResponse(data, safe=False)
		
	return render(request, 'html/search.html')
