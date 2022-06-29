from django.shortcuts import render, redirect

from main.form import *
# Create your views here.
from .models import *
def index(request):
    kurs = Kurs.objects.all()
    ctx = {
        "kurs": kurs
    }
    return render(request, "main/base.html",ctx)
def categoriya(request):
    kurs = Kurs.objects.all()

    ctx = {
        "kurs":kurs
    }
    return render(request,"kategoriya/index_categoriya.html",ctx)

def guruh(request):
    kurs = Kurs.objects.all()
    ctx = {
        "kurs": kurs
    }
    return render(request, "guruhlar/guruh.html", ctx)

def guruhlar(request,id):
    kurs = Kurs.objects.all()
    guruh = Guruh.objects.filter(kurs_id=id)
    talaba = Talaba.objects.filter(guruh_id=id)
    ctx = {
        "talaba":talaba,
        "kurs":kurs,
        "guruh":guruh
    }
    return render(request,"guruhlar/guruh.html",ctx)


def talaba(request):
    kurs = Kurs.objects.all()
    ctx = {
        "guruh":guruh,
        "kurs": kurs
    }
    return render(request, "talaba/talaba.html", ctx)

def talaba_id(request,id):
    kurs = Kurs.objects.all()
    guruh = Guruh.objects.filter(kurs_id=id)
    talaba = Talaba.objects.filter(guruh_id=id)
    ctx = {
        "kurs":kurs,
        "guruh":guruh,
        "talaba":talaba
    }
    return render(request, "talaba/talaba.html", ctx)