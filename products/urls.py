from django.urls import path

from  .views import (product_detail_view,
                            product_create_view,
                            product_add_view,
                            product_edit_view,
                            product_delete_view,
                            product_list)

urlpatterns = [
	path('product/<int:my_id>', product_detail_view,name='product-detail'),
    path('create/', product_create_view),
    path('add/', product_add_view),
    path('list-product/', product_list),
    path('edit-product/<int:my_id>/', product_edit_view),
    path('delete-product/<int:my_id>/', product_delete_view),
]