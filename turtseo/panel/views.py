from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
# from . models import 
from django.views.decorators.csrf import csrf_exempt

import csv

@csrf_exempt
def FileUpload(request):
	print("File Upload")
	
	if request.method == "POST":
		exelFile = request.FILES.get('file')
		fileName = str(exelFile)
		print(fileName)

		data = "C:\\Users\\hasan\\Downloads\\" + fileName
		print(data)

		with open(data, mode='r') as csv_file:
			csv_reader = csv.reader(csv_file)
			line_count = 0
			for row in csv_reader:
				if line_count == 0:
					print(f'Column names are {", ".join(row)}')
					line_count += 1

				print(row["#"])
				line_count += 1
			print(f'Processed {line_count} lines.')

		print("Success")


		# print(exelData['Referring Page URL'])

	# return HttpResponse("OK")
	return render(request, 'html/index.html')




# @csrf_exempt
# def add_data(request):
# 	print("request aise")
# 	# if request.method == 'POST':
# 	# 	linkid = request.POST['linkid']
# 	# 	exampleFormControlFile1 = request.POST['exampleFormControlFile1']
# 	# 	tagarea = request.POST['tagarea']
# 	# 	niche = request.POST['niche']
# 	# 	dr = request.POST['dr']
# 	# 	da = request.POST['da']
# 	# 	spamscore = request.POST['spamscore']
# 	# 	traffic = request.POST['traffic']
# 	# 	existingcost = request.POST['existingcost']
# 	# 	newCost = request.POST['new Cost']
# 	# 	email = request.POST['email']		

# 	# return HttpResponse("Data Entry")
# 	# return an object to HTML page 
# 	# get cols
# 	return render(request, 'html/index.html')