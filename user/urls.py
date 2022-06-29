from django.urls import path
from user.views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('login/', dashboard_login, name="login"),
    path('logout/', dashboard_logout, name="logout"),


]