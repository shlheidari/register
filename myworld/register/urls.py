from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('signup/addrecord/', views.addrecord, name='addrecord'),
    path('login/loging/', views.loging, name='loging'),
    path('loged_in/', views.loged_in, name='loged_in'),
]
