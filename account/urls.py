from django.urls import path
from . import views


urlpatterns = [
    path('',views.handlelogin, name='handlelogin'),
    path('logout/',views.handlelogout, name='handlelogout'),
    path('register/',views.register, name='register'),
    path('error/',views.error, name='error'),
    path('editprofile/',views.editprofile, name='editprofile'),
]
