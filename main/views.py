from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, logout as _logout, login as _login
from .models import *

def index(request):
    return render(request, "Main/home.html")

def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")

    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        auth = authenticate(username=username, password=password)
        if auth is not None:
            _login(request, auth)
            return render(request, "Main/login.html", {'success':True})
        else:
            return render(request, "Main/login.html", {'error': True, 'message':'User Does Not Exist'})
    return render(request, "Main/login.html")

def logout(request):
    _logout(request)
    return HttpResponseRedirect("/")

def redirect_to_dashboard(request):
    user_details = UserDetails.objects.filter(user=request.user).last()
    if request.user.is_superuser:
        return HttpResponseRedirect("/main_admin_dashboard")
    elif user_details.role == "Branch Admin":
        return HttpResponseRedirect("/branch_admin_dashboard")