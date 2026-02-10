from django.urls import path, include
from . import views

urlpatterns = [
    # Pages
    path('', views.home, name='home'),
    path('movies/', views.movie_list, name='movie_list'),
    path('books/', views.book_list, name='book_list'),
    
    # Detail Page (The "Separate Page" you asked for)
    path('item/<int:pk>/', views.item_detail, name='item_detail'),

    # User Actions
    path('add/', views.add_media, name='add_media'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')), # Built-in Login/Logout

    # API (Keep this for Assignment 8)
    path('api/media/', views.media_list_api, name='media_list_api'),
    path('api/media/<int:pk>/', views.media_detail_api, name='media_detail_api'),
]