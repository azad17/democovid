from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'User Exists !')
                return redirect('userapp:register')
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email taken !')
                return redirect('userapp:register')
            user = User.objects.create_user(username=username,email=email,password=password)
            user.save
            return redirect ('userapp:login')
        else:
            messages.info(request,"Passwords aren't matching !")
            return redirect('userapp:register')
    return render(request,'userapp/register.html')
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Username/Password is Incorrect')
            redirect('userapp:login')
    return render(request,'userapp/login.html')
def logout(request):

    auth.logout(request)
    return redirect('/')