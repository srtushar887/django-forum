from django.urls import path

from . import views

urlpatterns = [
    path('loginUser',views.loginUser,name="loginUser"),
    path('register',views.register,name="register"),
    path('logout',views.logout,name="logout"),
    path('profile',views.my_profile,name="my_profile"),
]