from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:menu_type_slug>/', views.menu_detail, name='menu_detail'), 
    path('category/<slug:category_slug>/', views.category_detail, name='category_detail'),
    path('dish/<str:dish_name>/', views.dish_detail, name='dish_detail'), 
]