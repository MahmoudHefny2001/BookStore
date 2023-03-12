from django.urls import path, include
from . import views
from django.conf import settings 
from django.conf.urls.static import static 

app_name = 'store'

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('item/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search/<slug:category_slug>/', views.category_list, name='category_list'),
]