from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.


def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['conpass']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                print("username taken")
            elif User.objects.filter(email=email).exists():
                print("Email already taken")
            else:        
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                print('user created')
        else:
            print("password doesn't match")
        return redirect('/')
    else:         
        return render(request,'register.html')      

        
                  

            

        
                          

                        


             
         
        

        

