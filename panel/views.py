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

		serialized = serializers.serialize('json', link_counter_object)
		data = {"dataset": serialized}

		return JsonResponse(data, safe=False)
	else:
		return render(request, 'html/search.html')


@csrf_exempt
def Search_Url_list(request):
	if request.method == "POST":
		searched_key_Link = request.POST.get('key_data')
		compare_key_Link = request.POST.get('compare_data')
		
		searched_key_Link_urls = Profile.objects.filter(key_link=searched_key_Link) #all url of searched key_link
		compare_key_Link_urls = Profile.objects.filter(key_link=compare_key_Link) #all url of compare key_link
		
		matched_url = []	
		for i in searched_key_Link_urls:
			for j in compare_key_Link_urls:			
				if(i.url == j.url):
					matched_url.append(i.url)
		
		matched_key_link = []
		for obj in matched_url:
			if(Key_Link_List.objects.filter(key_link = obj)):
				matched_key_link.append(1)
			else:
				matched_key_link.append(0)
		
		url_data = json.dumps({'url' : matched_url, 'isKey': matched_key_link})
		return JsonResponse(url_data, safe=False)

	else:
		return render(request, 'html/url_list.html')


@csrf_exempt
def Directory(request):

	if request.method == "POST":
		btnpressed = request.POST.get('btnpressed')

		# Directory Name Model
		if(btnpressed == 'createdir'):
			dirname = request.POST.get('dirname')

			directory_name_model = DirectoryName(
				directory_name = dirname
			)
			directory_name_model.save()

			directory_name_foreign_key = DirectoryName.objects.get(directory_name = dirname)

			directory_item = DirectoryItem(
				directory_name = directory_name_foreign_key,
				key_link = "Facebook.com"
			)
			directory_item.save()

			directory_item = DirectoryItem(
				directory_name = directory_name_foreign_key,
				key_link = "Google.com"
			)
			directory_item.save()

			return render(request, 'html/directory.html')

		# Search Directory
		elif btnpressed == 'search':
			searchdir = request.POST.get('searchdir')

			if( DirectoryName.objects.filter(directory_name = searchdir).count() == 1):
				
				linked_key_list = DirectoryItem.objects.filter(directory_name = searchdir)
				serialized = serializers.serialize('json', linked_key_list)
				
				data = {"dataset": serialized}
				return JsonResponse(data, safe=False)
			else:
				return HttpResponseNotFound("No Directory Found")

		elif btnpressed == "initial":
			key_link_list = Key_Link_List.objects.all()
			serialized = serializers.serialize('json', key_link_list)
			
			data = {"dataset": serialized}
			return JsonResponse(data, safe=False)

		else:
			search_key_text = request.POST.get('search_key_text')

			# key_link_list_object = Key_Link_List.objects.filter(key_link = search_key_text)

			if(Key_Link_List.objects.filter(key_link = search_key_text).count() == 1):
				key_link_list = Key_Link_List.objects.filter(key_link = search_key_text)

				serialized = serializers.serialize('json', key_link_list)
				
				data = {"dataset": serialized}
				return JsonResponse(data, safe=False)

			else:
				HttpResponseNotFound("No Link Found")
				
	
	else:
		return render(request, 'html/directory.html')