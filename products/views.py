from django.shortcuts import render
from django.http import HttpResponse

from .models import Product

from .forms	 import ProductForm
# Create your views here.
def product_detail_view(request):
	obj = Product.objects.get(id=1)
	# context = {
	# 	'title':obj.title,
	# 	'description':obj.description,
	# }
	context = {
		'object' : obj
	}
	return render(request,"product/product_details.html",context)



def product_create_view(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		context = {
			'message': "Successfully added"
		}
	else :
		context = {
			'form': form
		}
	return render(request,"product/product_create.html",context)