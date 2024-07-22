from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_food, name='search_food'),
    path('addfood/<int:food_id>/', views.addfood, name='addfood'),
    path('total_carbon/', views.total_carbon, name='total_carbon'),
    path('clear/', views.clear_food_list, name='clear_food_list'),
    path('about/', views.about, name='about'),
    path('wishlist/', views.view_wishlist, name='view_wishlist'),
    path('add_to_wishlist/', views.add_to_wishlist, name='add_to_wishlist'),
    path('food_list/', views.food_list, name='food_list'),  # 新增这行
]
