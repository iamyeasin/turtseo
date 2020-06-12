from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404
from . models import *
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers


#save key_link in Key_Link_List model
def Model_Key_Link_List_Save(key_link_name):
    key_link_list_model = Key_Link_List(
        key_link = key_link_name
    )

    key_link_list_model.save()

    return HttpResponse("OK")


#save key_link with url & domanin_rank in Profile model
def Model_Profile_Save(key_link_name, URLList, DRList):
    # All csv data save under POST key link given by USER
    key_link_list_foreign_key = Key_Link_List.objects.get(key_link=key_link_name)
    
    data_size = len(URLList)
    for i in range(data_size):
        profile = Profile(
            key_link = key_link_list_foreign_key,
            url = URLList[i],
            domanin_rank = DRList[i],
        )

        profile.save()

    return HttpResponse("OK")


#calculating matched url with two key_link and stroing in the Link_Counter model
def Model_Link_Counter_Save(key_link_name, URLList):
    # Foreign Key access
    key_link_list_foreign_key = Key_Link_List.objects.get(key_link=key_link_name)
    key_link_list_object = Profile.objects.filter(key_link=key_link_list_foreign_key)

    total_url_in_key_link = len(key_link_list_object)

    isEmpty = Link_Counter.objects.count()

    # if Model is empty then Data inserted into Model
    if(isEmpty == 0):
        link_counter_model = Link_Counter(
            key_link = key_link_list_foreign_key,
            compare_key_link = key_link_list_foreign_key,
            no_of_data_matched = total_url_in_key_link,
            compare_key_link_no_of_data = total_url_in_key_link,
        )
        link_counter_model.save()
    
    else:
        # first grab all the objects contains in Link Counter Model
        key_link_list_model_object = Key_Link_List.objects.all()

        # Match with own key link
        link_counter_model = Link_Counter(
            key_link = key_link_list_foreign_key,				# Post Key Link
            compare_key_link = key_link_list_foreign_key,		# Post Key Link
            no_of_data_matched = total_url_in_key_link,
            compare_key_link_no_of_data = total_url_in_key_link,
        )
        link_counter_model.save()

        # match with other key link in KEY LINK LIST Model
        for link in key_link_list_model_object:
            key = link.key_link   	# Link Counter Model er key link

            new_key_link_objects_url = Profile.objects.filter(key_link=key)		# Object of Profile Model
            matched_url_counter = 0
            data_size = len(URLList)

            # Nested Loop for url matched in both key link
            for obj in new_key_link_objects_url:
                for i in range(data_size):
                    if(obj.url == URLList[i]):
                        matched_url_counter = matched_url_counter + 1

            # Foreign Key access
            foreignKey = Key_Link_List.objects.get(key_link=key)

            # IF data wasn't inserted then insert data [Format: A -> B]
            if(Link_Counter.objects.filter(key_link = foreignKey, compare_key_link = key_link_list_foreign_key).count() == 0):
                link_counter_model = Link_Counter(
                    key_link = foreignKey,							# Model Key Link
                    compare_key_link = key_link_list_foreign_key,	# Post Key Link
                    no_of_data_matched = matched_url_counter,
                    compare_key_link_no_of_data = data_size,
                )
                link_counter_model.save()

            # IF data wasn't inserted then insert data [Format: B -> A]
            total_url_in_model_key_link = Profile.objects.filter(key_link=key)			# Profile Model Object

            if(Link_Counter.objects.filter(key_link = key_link_list_foreign_key, compare_key_link = foreignKey).count() == 0):
                link_counter_model = Link_Counter(
                    key_link = key_link_list_foreign_key,			# Post Key Link
                    compare_key_link = foreignKey,					# Model Key Link
                    no_of_data_matched = matched_url_counter,
                    compare_key_link_no_of_data = len(total_url_in_model_key_link),
                )
                link_counter_model.save()
    
    return HttpResponse("OK")


#storing all about of a key_link in Profile_Extended model
def Model_Profile_Extended_Save(key_link_name, post_dr, post_da, post_traffic, post_spamscore, post_existingcost, post_new_Cost, post_email, post_niche):
    # Foreign Key access
    key_link_list_foreign_key = Key_Link_List.objects.get(key_link=key_link_name)

    profile_extended_model = Profile_Extended(
        key_link = key_link_list_foreign_key,	# Key Link List Foreign Key
        domanin_rank = post_dr,
        domanin_auth = post_da,
        traffic = post_traffic,
        spam_score = post_spamscore,
        existing_cost = post_existingcost,
        new_cost = post_new_Cost,
        email = post_email,
        niche = post_niche,
    )
    profile_extended_model.save()

    return HttpResponse("OK")
