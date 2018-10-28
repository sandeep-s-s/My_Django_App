from django.shortcuts import render
from django.http import HttpResponse

from .models import Product
# Create your views here.
def product_detail_view(request):
	obj = Product.objects.get(id=1)
	context = {
		'title':obj.title,
		'description':obj.description,
	}
	return render(request,"product/detail.html",context)