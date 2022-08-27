from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path(r'^login$', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path(r'^signup$', views.signup, name='signup'),
    path('signup/addrecord/', views.addrecord, name='addrecord'),
    path('addrecord/', views.addrecord, name='addrecord'),
    path('login/loging/', views.loging, name='loging'),
    path('loging/', views.loging, name='loging'),
    path('loged_in/<str:user_name>', views.loged_in, name='loged_in'),
    path('login/forget/', views.forget, name='forget'),
    path('forget/', views.forget, name='forget'),
    path('login/forget/check/', views.check, name='check'),
    path('forget/check/', views.check, name='check'),
    path('checked/<str:user_name>', views.checked, name='checked'),
    path('checked/reset/<str:user_name>', views.reset, name='reset'),
    path('loged_in/delete/<str:user_name>', views.delete, name='delete'),
    path('loged_in/change/<str:user_name>', views.change, name='change'),
]
