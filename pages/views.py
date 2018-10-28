from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request ,*args,**kwargs):
	print(request.user,args,kwargs)
	# return HttpResponse('<h1>Hello World !!</h1>')
	thisdict =	{
  		"brand": "Ford",
  		"model": "Mustang",
  		"year" : 1964,
  		"car"  : ["Ford", "Volvo", "BMW",123] ,
  		"html" : "<h1>Hello test for filter</h1>" #Test for template tag and filter
	}
	return render(request,"home.html",thisdict)

def about_view(request,*args,**kwargs):
	return render(request,"about.html",{})

def contact_view(request,*args,**kwargs):
	return render(request,"contact.html",{})
