from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout

# Create your views here.

def custom(request):
    return render(request,'index.html')

def Register(request):
   context={}
   if request.method=="GET":
        return render(request,'register.html')
   else:
        n=request.POST['uname']
        p=request.POST['upass']
        cp=request.POST['ucpass']

        if n=='' or p=='' or cp==''or n!=".": 
            context['errmsg']="Fields cannot be blank or use (.) for mayur "
            return render(request,'register.html',context)
        elif p!=cp:
            context['errmsg']="Password and confirm password didnt match "
            return render(request,'register.html',context)
        elif len(p)<8:
            context['errmsg']="Password must be minimum Eight Character"
            return render(request,'register.html',context)
        else:
            try:
                u=User.objects.create(username=n,password=p)
                u.set_password(p)
                u.save()
                context['success']="User Created Successfully"
                return render(request,'register.html',context)
            except Exception:
                context['errmsg']=" User Already Exists"
                return render(request,'register.html',context)
            
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login  # Renaming to avoid conflicts

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        n = request.POST.get('uname')
        p = request.POST.get('upass')

        # Authenticate the user
        user = authenticate(username=n, password=p)

        if user is not None:
            # Log the user in
            auth_login(request, user)  # Renamed login function to auth_login
            return redirect('/custom')  # Redirect to the desired URL upon successful login
        else:
            context = {'errmsg': "Invalid username or password"}
            return render(request, 'login.html', context)

        
def user_logout(request):
    logout(request)        
    return redirect('/custom')

    
        