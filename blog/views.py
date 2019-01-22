from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.views.generic import (
		ListView,DetailView,CreateView,UpdateView,DeleteView
	)

from .models import Blog

from .forms import BlogForm

class BlogListView(ListView): # blog/modelname_list.html // expected view oR
	template_name = 'blog/blog_list.html' 
	queryset = Blog.objects.all();

class BlogDetailView(DetailView):
	template_name = 'blog/blog_details.html'  
	# queryset = Blog.objects.all() #for pk or slug instead of id in urls.py

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Blog,id=id_)


class BlogCreateView(CreateView):
	template_name = 'blog/blog_create.html'  
	form_class=	BlogForm	
	# success_url='/'
	# queryset = Blog.objects.all();

class BlogUpdateView(UpdateView):
	template_name = 'blog/blog_create.html'
	form_class=BlogForm
	queryset = Blog.objects.all();
	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Blog,id=id_)  

class  BlogDeleteView(DeleteView):
	template_name = 'blog/blog_delete.html'
	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Blog,id=id_)  

	def get_success_url(self):
		return reverse('blog-list')