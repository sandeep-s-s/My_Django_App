from django.shortcuts import render,get_object_or_404,redirect

from django.http import HttpResponse

from .models import Product

from .forms	 import ProductForm

from .forms	 import RawProductForm


from django.http import Http404


from django.http import HttpResponseRedirect


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


def product_add_view(request):
	initial_data =	{
						'title' : "Default title"
					}
	form =RawProductForm(request.POST or None,initial=initial_data)
	context = {
		'form': form
	}
	if request.method == "POST" :
		# form =RawProductForm(request.POST)
		if form.is_valid() :
			Product.objects.create(**form.cleaned_data)
	return render(request,"product/product_add.html",context)
	

def product_edit_view(request,my_id):
	try:
		obj = Product.objects.get(id=my_id)
		form =ProductForm(request.POST or None,instance=obj)
		if form.is_valid():
			form.save()
		context = {
			'form': form
		}
		return render(request,"product/product_edit.html",context)	
	except Product.DoesNotExist:
		raise Http404

def product_delete_view(request,my_id):
	obj = get_object_or_404(Product,id=my_id)
	if request.method == "POST":
		obj.delete()
		return HttpResponseRedirect("/home/")
	else :
		context = {
			'object' : obj
		}
		return render(request,"product/product_delete.html",context)	


def product_list(request):
	queryset = Product.objects.all();
	context = {
		"object_list" : queryset
	}
	return render(request,"product/product_list.html",context)	