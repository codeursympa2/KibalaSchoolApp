from django.urls import path
from .views import * 
urlpatterns=[
    path('',login_blog,name="connexion"),
    path('logout',logout_view,name="logout"),
    path('password-change',change_view,name="change_password")
]