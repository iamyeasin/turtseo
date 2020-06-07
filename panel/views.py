from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404
from . models import *
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

import json

@csrf_exempt
def FileUpload(request):
	print("Class: File Upload")
	
	if request.method == 'POST':
		post_key_link = request.POST.get('key_link')
		URLList = request.POST.getlist('urlList[]')
		DRList = request.POST.getlist('drList[]')

		# Key Link Model

		key_link_model = Key_Link_List()
		key_link_model.key_link = post_key_link
		key_link_model.save()

		# Profile Model
		# All csv data save under POST key link given by USER

		key_id = Key_Link_List.objects.get(key_link=post_key_link)
		data_size = len(URLList)

		for i in range(data_size):
			profile = Profile(
				key_link = key_id,
				url = URLList[i],
				domanin_rank = DRList[i],
			)
			profile.save()

		print("Data Saved into Model")

		# Link Counter Model

		# Foreign Key access
		key_id = Key_Link_List.objects.get(key_link=post_key_link)
		key_link_list_object = Profile.objects.filter(key_link=key_id)

		total_url_in_key_link = len(key_link_list_object)

		isEmpty = Link_Counter.objects.count()

		# if Model is empty then Data inserted into Model

		if(isEmpty == 0):
			link_counter_model = Link_Counter(
				key_link = key_id,
				compare_key_link = key_id,
				no_of_data_matched = total_url_in_key_link,
				compare_key_link_no_of_data = total_url_in_key_link,
			)
			link_counter_model.save()
		
		# if Model is not empty

		else:
			print("Nirob Chutiya")

			# first grab all the objects contains in Link Counter Model

			key_link_list_model_object = Key_Link_List.objects.all()

			# Match with own key link

			print(key_id)

			link_counter_model = Link_Counter(
				key_link = key_id,				# Post Key Link
				compare_key_link = key_id,		# Post Key Link
				no_of_data_matched = total_url_in_key_link,
				compare_key_link_no_of_data = total_url_in_key_link,
			)
			link_counter_model.save()

			# match with other key link in KEY LINK LIST Model

			for link in key_link_list_model_object:
				key = link.key_link   							# Link Counter Model er key link

				new_key_link_objects_url = Profile.objects.filter(key_link=key)		# Object of Profile Model

				matched_url_counter = 0

				# Nested Loop for url matched in both key link

				for obj in new_key_link_objects_url:
					for i in range(data_size):
						if(obj.url == URLList[i]):
							matched_url_counter = matched_url_counter + 1

				# Foreign Key access

				foreignKey = Key_Link_List.objects.get(key_link=key)

				# IF data wasn't inserted then insert data [Format: A -> B]
				if(Link_Counter.objects.filter(key_link = foreignKey, compare_key_link = key_id).count() == 0):
					link_counter_model = Link_Counter(
						key_link = foreignKey,							# Model Key Link
						compare_key_link = key_id,						# Post Key Link
						no_of_data_matched = matched_url_counter,
						compare_key_link_no_of_data = data_size,
					)
					link_counter_model.save()


				# IF data wasn't inserted then insert data [Format: B -> A]
				total_url_in_model_key_link = Profile.objects.filter(key_link=key)			# Profile Model Object

				if(Link_Counter.objects.filter(key_link = key_id, compare_key_link = foreignKey).count() == 0):
					link_counter_model = Link_Counter(
						key_link = key_id,								# Post Key Link
						compare_key_link = foreignKey,					# Model Key Link
						no_of_data_matched = matched_url_counter,
						compare_key_link_no_of_data = len(total_url_in_model_key_link),
					)
					link_counter_model.save()


		# Profile Extended Model

		post_niche = request.POST.get('niche')
		post_dr = request.POST.get('dr')
		post_da = request.POST.get('da')
		post_spamscore = request.POST.get('spamscore')
		post_traffic = request.POST.get('traffic')
		post_existingcost = request.POST.get('existingcost')
		post_new_Cost = request.POST.get('new_cost')
		post_email = request.POST.get('email')

		profile_extended_model = Profile_Extended(
			key_link = key_id,						# Key Link List Foreign Key
			domanin_auth = post_da,
			traffic = post_traffic,
			spam_score = post_spamscore,
			existing_cost = post_existingcost,
			new_cost = post_new_Cost,
			email = post_email,
			niche = post_niche,
		)

		profile_extended_model.save()

		print("Data Saved")
				
	else:
		print("No Data Found")
	
	return render(request, 'html/index.html')


@csrf_exempt
def Search(request):

	print("Search Class")

	if request.method == "POST":
		search_key = request.POST.get('search_key')
		print(search_key)

		link_counter_object = Link_Counter.objects.filter(key_link = search_key)

		serialized = serializers.serialize('json', link_counter_object)

		data = {"dataset": serialized}
		return JsonResponse(data, safe=False)

	else:
		return render(request, 'html/search.html')
