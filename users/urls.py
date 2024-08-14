from django.urls import path
from .views import *

urlpatterns=[
    path('login/',userLogin,name="login"),
    path('register/',userRegister,name="register"),
    path('comunucation/',comunucation,name="comunucation"),
    path('logout/',userLogout,name="logout"),
    path('delete/',deleteAccount,name="delete"),
    path('account/',account,name="account"),
]