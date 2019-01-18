from django.shortcuts import render

from django.views.generic import ListView

from .models import Blog

class BlogListView(ListView): # blog/modelname_list.html // expected view oR
	template_name ='blog/blog_list.html' 
	queryset = Blog.objects.all();

