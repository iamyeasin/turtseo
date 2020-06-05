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


def Search(request):	
	if(request.method == 'POST'):
		link = request.POST['keyLink']		
		
		queryLinks = Profile.objects.filter(key_link__key_link__icontains=link) #grab requested keylink profile from database
		
		dicts = {}
		key_Links = Key_Link_List.objects.all() #grab all keylink from database
		for key_Link in key_Links:
			k_link = key_Link.key_link
			dicts[k_link] = 0

		for queryLink in queryLinks:			
			for key_Link in key_Links:

				qLink = queryLink.url
				k_link = key_Link.key_link

				links_in_profils = Profile.objects.filter(key_link__key_link__icontains=k_link)
				
				for links_in_profil in links_in_profils:										
					if qLink == links_in_profil.url:
						val = dicts.get(k_link)
						dicts[k_link] = val+1				

		context = {
			'dataList': dicts,
			'link_list' : queryLinks,
			'search_link' : link
		}		
		return render(request, 'html/search.html', context)	
	return render(request, 'html/search.html')	
