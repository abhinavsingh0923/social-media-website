from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    # path('message/',views.chatting,name='chatting'),
    path('profile/',views.profilepage,name='profilepage'),
    # path('editprofile/',views.editprofilepage,name='editprofilepage'),
    path('addpost/',views.addpostfunction,name='addpostfunction'),
    path('like/',views.like_post,name='like_post'),
    path('search',views.search,name='search'),
    path('follow/',views.follow,name='follow'),
    path('otherprofilepage/<str:pk>/',views.otherprofilepage,name='otherprofilepage'),
]
