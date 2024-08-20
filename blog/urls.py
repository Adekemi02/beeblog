from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.post, name='post'),
    path('post/search/', views.search_by_category, name='search'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
]