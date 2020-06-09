from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404
from . models import *
from . import methods
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
# from urllib import parse
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

		# for i in link_counter_object:
		# 	print(i.no_of_data_matched)

		serialized = serializers.serialize('json', link_counter_object)

		data = {"dataset": serialized}
		return JsonResponse(data, safe=False)
	else:
		return render(request, 'html/search.html')


@csrf_exempt
def  Search_Url_list(request):
	if request.method == "POST":
		searched_key_Link = request.POST.get('key_data')
		compare_key_Link = request.POST.get('compare_data')
		print(searched_key_Link)
		print(compare_key_Link)

		key_Links = Key_Link_List.objects.all() # all key_link from Key_Link_List table			
		searched_key_Link_urls = Profile.objects.filter(key_link=searched_key_Link) #all url of searched key_link
		compare_key_Link_urls = Profile.objects.filter(key_link=compare_key_Link) #all url of compare key_link
		
		matched_url = {}	
		for i in searched_key_Link_urls:
			for j in compare_key_Link_urls:			
				if(i.url == j.url):
					matched_url[i.url] = 0
		
		for key,val in matched_url.items():						
			for link in key_Links:													
				if(str(key) == str(link)): 
					matched_url[key] = 1
		
		for k,v in matched_url.items():
			print(k,v)
		
		url_data = json.dumps({ 'url_list' : matched_url})
		return JsonResponse(url_data, safe=False)

	else:
		return render(request, 'html/search.html')		
