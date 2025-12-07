
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from myapp import views

urlpatterns = [
    re_path(r"^products/(?P<productid>\d+)", views.products),
    re_path(r'^users/(?P<id>\d+)/(?P<name>\D+)/', views.users),
    path('products-category/<int:productid>/', views.products_category),
    path('user/', views.user),
    re_path(r'^about/contact/', views.contact),
    re_path(r'^about', views.about),
    path('', views.index)
]
