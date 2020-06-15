from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404
from . models import *
from . import methods
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json


#All about "Turtseo Data Panel/Home" page:
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

		post_key_link = post_key_link.lower()

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


#All about "Turtseo Search Panel/Search" page:
@csrf_exempt
def Search(request):
	if request.method == "POST":
		search_key = request.POST.get('search_key')
		search_key = search_key.lower()

		#search by Foreign Key
		link_counter_object = Link_Counter.objects.filter(key_link = search_key)

		serialized = serializers.serialize('json', link_counter_object)
		data = {"dataset": serialized}

		return JsonResponse(data, safe=False)

	else:
		return render(request, 'html/search.html')


#All about "Show URL" button & "URL List Panel" in "Search" page:
@csrf_exempt
def Search_Url_list(request):
	if request.method == "POST":
		searched_key_Link = request.POST.get('key_data')
		compare_key_Link = request.POST.get('compare_data')
		searched_key_Link = searched_key_Link.lower()
		compare_key_Link = compare_key_Link.lower()
		
		#all url of searched key_link
		searched_key_Link_urls = Profile.objects.filter(key_link=searched_key_Link)
		#all url of compare key_link
		compare_key_Link_urls = Profile.objects.filter(key_link=compare_key_Link)
		
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


#All about "Turtseo Directories/Directory" page:
@csrf_exempt
def Directory(request):
	if request.method == "POST":
		btnpressed = request.POST.get('btnpressed')


		#delete key_link from DirectoryItem model
		if(btnpressed == "delLinktodir"):
			try:
				dirname = request.POST.get('dirname').strip()
				guestlink = request.POST.get('url').strip()
				dirname = dirname.lower()
				guestlink = guestlink.lower()

				DirectoryItem.objects.filter(directory_name=dirname , key_link=guestlink).delete()

				return HttpResponse("Delete Completed")

			except:
				return HttpResponse("Delete Operation couldn't Complete")


		#add new key_link to DirectoryItem model
		elif( btnpressed == 'addlinktodir' ):
			try:
				dirname = request.POST.get('dirname').strip()
				guestlink = request.POST.get('url').strip()
				dirname = dirname.lower()
				guestlink = guestlink.lower()


				directory_name_model = DirectoryName(
					directory_name = dirname
				)
				directory_name_foreign_key = DirectoryName.objects.get(directory_name = dirname)

				isAvail = None

				try:
					isAvail = DirectoryItem.objects.get(directory_name=directory_name_foreign_key, key_link=guestlink)
				
				except:
					isAvail = None

				if isAvail == None:
					directory_item = DirectoryItem(
						directory_name = directory_name_foreign_key,
						key_link = guestlink
					)
					
					directory_item.save()

					return HttpResponse("Saved the data")

				else:
					return HttpResponseNotFound("Duplicate Entry exists")

			except Exception as e:
				return HttpResponse(e)


		#create a new directory in DirectoryName model
		elif(btnpressed == 'createdir'):
			dirname = request.POST.get('dirname').strip()
			dirname = dirname.lower()

			if( DirectoryName.objects.filter(directory_name = dirname).count() == 1):				
				return HttpResponseNotFound("Duplicate Directory exists")

			else:
				directory_name_model = DirectoryName(
					directory_name = dirname
				)
				directory_name_model.save()		

				return render(request, 'html/directory.html')


		#search directory with all key_link from DirectoryName & DirectoryItem model
		elif btnpressed == 'search':
			searchdir =  request.POST.get('searchdir').strip()
			searchdir = searchdir.lower()

			if( DirectoryName.objects.filter(directory_name = searchdir).count() == 1):		
				linked_key_list = DirectoryItem.objects.filter(directory_name = searchdir)
				serialized = serializers.serialize('json', linked_key_list)
				
				data = {"dataset": serialized}

				return JsonResponse(data, safe=False)

			else:
				return HttpResponseNotFound("No Directory Found")


		#show all key_link initially in Turtseo Directories page from Key_Link_List model
		elif btnpressed == "initial":
			key_link_list = Key_Link_List.objects.all()
			serialized = serializers.serialize('json', key_link_list)
			data = {"dataset": serialized}
			return JsonResponse(data, safe=False)


		#search key_link from Key_Link_List model by autocomplete search in Turtseo Directories page
		else:
			searchres =  request.POST.get('search').strip()
			searchres = searchres.lower()	

			key_link_list_object = Key_Link_List.objects.filter(key_link = searchres)

			query = None

			try:
				query = Key_Link_List.objects.filter(key_link = searchres)

			except:
				query = None

			if( query != None):
				key_link_list = None

				try:
					key_link_list = Key_Link_List.objects.filter(key_link__contains = searchres)

				except:
					key_link_list = None
				
				if key_link_list != None:
					serialized = serializers.serialize('json', key_link_list)

					data = {"dataset": serialized}

					return JsonResponse(data, safe=False)

				else:
					return HttpResponseNotFound("No data found")

			else:
				HttpResponseNotFound("No Link Found")
				
	else:
		return render(request, 'html/directory.html')


#All about  "All Directory" button in "Turtseo Directories/Directory" page:
@csrf_exempt
def Directory_List(request):

	if request.method == "POST":
		btnpressed = request.POST.get('btnpressed')
		

		#Show all directory initially in "Directory List" page
		if btnpressed == "load_all_directory":

			try:
				directory_name_model = DirectoryName.objects.all();

			except:
				directory_name_model = None
			
			if directory_name_model != None:
				serialized = serializers.serialize('json', directory_name_model)
				data = {"dataset": serialized}

				return JsonResponse(data, safe=False)

			else:
				return HttpResponseNotFound("No data found")


		#Delete a directory from "Directory" or "Directory List" page
		elif(btnpressed == "delete_directory"):
			try:
				dirname = request.POST.get('dirname').strip()
				dirname = dirname.lower()

				DirectoryName.objects.filter(directory_name=dirname).delete()

				return HttpResponse("Delete Completed")

			except:
				return HttpResponse("Delete Operation couldn't Complete")

	return render(request, 'html/directory_list.html')