from django.urls import path
from .views import (BlogListView,BlogDetailView,BlogCreateView,BlogUpdateView)

urlpatterns = [
	path('blog/', BlogListView.as_view()),
	path('blog-detail/<int:id>', BlogDetailView.as_view(),name='blog-detail'),
	path('blog-create/', BlogCreateView.as_view()),
	path('blog-update/<int:id>', BlogUpdateView.as_view()),
]