from django.urls import path,include
from main.views import *

urlpatterns =[
    path("",index,name="index"),
    path("dashboard/",include("user.urls")),
    path('categoriya/', categoriya, name="categoriya"),
    path('guruh/', guruh, name="guruh"),
    path("guruhlar/<int:id>",guruhlar,name="guruhlar"),
    path("talaba/",talaba,name="talaba"),
    path("talaba_id/<int:id>",talaba_id,name="talaba_id"),
]