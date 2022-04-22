from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    # path('index', include('index.html'))
    path('contact/', views.create_contact, name='contact'),
    # path('product/', product, name='product')
    path('update_product/<int:pk>', views.update_product, name="update_product"),
    path('delete_product/<int:pk>', views.delete_product, name="delete_product"),
    path('create_product/', views.create_product, name="create_product"),
    path('delete_crocekry/<int:pk>', views.delete_crocekry, name="delete_crocekry"),
    path('update_crocekry/<int:pk>', views.update_crocekry, name="update_crocekry"),
    path('create_crocekry/', views.create_crocekry, name="create_crocekry"),
    # path('sign_in', views.login_user, name="sign_in"),
    # path('sign_up', views.register_user, name="sign_up"),
    # path('logout', views.logout_user, name="logout"),
path('register', RegisterUser.as_view(), name="register")
]
