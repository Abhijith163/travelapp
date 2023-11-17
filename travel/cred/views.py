from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth


# login
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
       
    
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid user")
            return redirect('login')
    return render(request,"login.html")



#registeration
def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username is already taken")
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email is already taken")
                return redirect('registration')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
                user.save()
                return redirect('login')
                messages.success(request,"User created successfully")
        else:
            messages.info(request,"Passwords not matching")
            return redirect('registration')
        return redirect('/')
    return render(request,'registration.html')

#logout
def logout(request):
    auth.logout(request)
    return redirect('/')
