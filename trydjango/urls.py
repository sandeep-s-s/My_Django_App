"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#pages view
from  pages import views

#Product view
from  products.views import (product_detail_view,
                            product_create_view,
                            product_add_view,
                            product_edit_view,
                            product_delete_view,
                            product_list)

#aslo works
# from  pages.views import home_view


urlpatterns = [
    # path('', home_view),
    path('', views.home_view),
    path('home/', views.home_view),
    path('about/', views.about_view),
    path('contact/', views.contact_view),
    path('product/', product_detail_view),
    path('create/', product_create_view),
    path('add/', product_add_view),
    path('list-product/', product_list),
    path('edit-product/<int:my_id>/', product_edit_view),
    path('delete-product/<int:my_id>/', product_delete_view),
    path('admin/', admin.site.urls),
]
 