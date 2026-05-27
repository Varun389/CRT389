from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('add-game/', views.add_game, name='add_game'),

    path('delete-game/<int:id>/', views.delete_game, name='delete_game'),

    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),

]