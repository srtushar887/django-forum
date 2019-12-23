from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('create-post',views.create_post,name="create_post"),
    path('insert/user/post',views.save_user_post,name="save_user_post"),
    path('post/details/<int:post_id>',views.porst_details,name="porst_details"),
]