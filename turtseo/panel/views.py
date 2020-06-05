from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from . models import *
from django.views.decorators.csrf import csrf_exempt

import json

@csrf_exempt
def FileUpload(request):
	print("Class: File Upload")
	
	if request.method == 'POST':
		key_link = request.POST.get('key_link')
		URLList = request.POST.getlist('urlList[]')
		DRList = request.POST.getlist('drList[]')

		# print(URLList)

		key_link_model = Key_Link_List()
		key_link_model.key_link = key_link
		key_link_model.save()

		key_id = Key_Link_List.objects.get(key_link=key_link)

		data_size = len(URLList)

		for i in range(data_size):
			# print(i)
			profile = Profile(
			key_link = key_id,
			url = URLList[i],
			domanin_rank = DRList[i],
			)
			profile.save()

		print("Data Saved into Model")

	else:
		print("No Data Found")
	
	return render(request, 'html/index.html')


@csrf_exempt
def Search(request):
	print("search")
	return render(request, 'html/search.html')