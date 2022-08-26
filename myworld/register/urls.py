from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('signup/addrecord/', views.addrecord, name='addrecord'),
    path('login/loging/', views.loging, name='loging'),
    path('loging/', views.loging, name='loging'),
    path('loged_in/', views.loged_in, name='loged_in'),
    path('login/forget/', views.forget, name='forget'),
    path('login/forget/check/', views.check, name='check'),
    path('forget/', views.forget, name='forget'),
    path('forget/check/', views.check, name='check'),
    path('checked/', views.checked, name='checked'),
    path('checked/reset/', views.reset, name='reset'),
    path('loged_in/delete/', views.delete, name='delete'),
    path(r'^login$', views.login, name='login'),
    path(r'^signup$', views.signup, name='signup'),
]
