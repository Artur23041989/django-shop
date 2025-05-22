from django.urls import path
from .views import (CategoryCreatedView, CategoryListView,
                    ProductListView, ProductCreatedView,
                    ProductDetailView)


app_name = 'staff'
urlpatterns = [
    path('categories/add/', CategoryCreatedView.as_view(), name='category_add'),
    path('categories/', CategoryListView.as_view(), name='categories'),

    path('products/add/', ProductCreatedView.as_view(), name='product_add'),
    path('products/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/', ProductListView.as_view(), name='products'),
]