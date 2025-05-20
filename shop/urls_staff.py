from django.urls import path
from .views import CategoryCreatedView, CategoryListView

app_name = 'staff'
urlpatterns = [
    path('categories/add/', CategoryCreatedView.as_view(), name='category_add'),
    path('categories', CategoryListView.as_view(), name='categories'),
]