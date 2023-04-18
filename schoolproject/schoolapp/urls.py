from . import views
from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo'),
    path('register',views.register,name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('add1', views.add, name='add'),
    path('success', views.success, name='sucess'),
    path('add', views.person_create_view, name='person_create_view'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'), # AJAX
]

