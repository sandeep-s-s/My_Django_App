from django.urls import path
from .views import (BlogListView,BlogDetailView,BlogCreateView,BlogUpdateView,BlogDeleteView)

urlpatterns = [
	path('blog/', BlogListView.as_view(),name='blog-list'),
	path('blog-detail/<int:id>', BlogDetailView.as_view(),name='blog-detail'),
	path('blog-create/', BlogCreateView.as_view()),
	path('blog-update/<int:id>', BlogUpdateView.as_view()),
	path('blog-delete/<int:id>', BlogDeleteView.as_view()),
]