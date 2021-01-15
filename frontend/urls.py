from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('archive', views.archive),
    path('archive/create', views.archive_create),
    path('archive/list', views.archive_list),
    path('archive/<int:archive_id>/', views.archive_images),
    path('archive/detail/<int:archive_id>/', views.archive_detail),
    path('archive/image_create/<int:archive_id>/', views.image_create),
    path('archive/image_detail/<int:image_id>/', views.image_detail),
]
