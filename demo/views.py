from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def dashboard(request):
    return render(request, "users/dashboard.html")

@login_required
def secure(request):
    return render(request, "users/dashboardlogin.html")
    #return HttpResponse('Secure page. <a href="/openid/login">Logout</a>') 