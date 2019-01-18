from django.urls import path
from .views import (BlogListView)

urlpatterns = [
	path('blog/', BlogListView.as_view()),
]