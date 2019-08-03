from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth, User
# Create your views here.

def login(request):
       
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']

            user=auth.authenticate(email=email, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/')

            else:
                messages.info(request,"invalid credentials") 
                return redirect('login') 

        else:      
            return render(request, 'login.html')