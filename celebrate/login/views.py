
from django.shortcuts import render, redirect
from django.contrib.auth.models import  auth
from django.contrib import messages
# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password = request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
             messages.info(request,"invalid credentials")
             return redirect('logout')   
              
    else:
        return render(request,'login.html')
