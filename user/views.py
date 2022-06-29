from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,  logout
# Create your views here.
def login_required_decorator(f):
    return login_required(f, login_url="login")

@login_required_decorator
def dashboard(request):

   return render(request, 'main/index.html')

def dashboard_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'dashboard/login.html')

@login_required_decorator
def dashboard_logout(request):
    logout(request)
    return redirect('login')

def categoriya(request):


    return render(request,'kategoriya/index_categoriya.html' )
