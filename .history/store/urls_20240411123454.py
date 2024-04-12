from django.urls import path

from . import views

urlpatterns=[
    path('',views.store,name='store'),
    path('<slug:category_slug>/',views.store,name='product_by_category'),
    path('<int:category_pk>/<int:product_pk>/',views.product_detail,name='product_detail'),
]
   