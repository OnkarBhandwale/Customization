from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout
import random
import string
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.http import JsonResponse
from django.views.decorators.http import require_POST


# Create your views here.


def custom(request):
    return render(request,'index.html')

# def validateEmail(request):
#         sub='Here is Your Otp for Verification!!!'
#         msg='Your OTP is Genrated.. Dont Share this OTP'
#         frm='omkarbhandwale4017@gmail.com'
#         u=User.objects.filter(id=request.user.id)
#         to=u[0].email
#         send_mail(
#             sub,
#             msg,
#             frm,
#             [to],
#             fail_silently=False 
#         )
#         return render(request,'register.html')
# def otpgenrater(request):
# # Generate a random number between 1 and 100
#     random_number = random.randint(1, 100)
#     print("Random number:", random_number)

def Register(request):
   context={}
   if request.method=="GET":
        return render(request,'register.html')
   else:
        n=request.POST['uname']
        p=request.POST['upass']
        cp=request.POST['ucpass']

        if n=='' or p=='' or cp=='' or n =='.': 
            context['errmsg']="Fields cannot be blank or use (.) "
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
        


def generate_verification_code():
    # Generate a random 6-character verification code
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def send_verification_email(email, verification_code):
    # Set your sender email address
    sender_email = "omkarbhandwale4017@gmail.com"  # Change this to your Gmail address

    # Setup SMTP server connection
    smtp_server = "smtp.gmail.com"
    smtp_port = 587  # For SSL, use 465 instead
    sender_password = "utzd jwyd jrby mlka"  # Change this to your app-specific password

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = "Verify Your Email"

    # Email body
    body = u"Your verification code is: " + verification_code
    body_encoded = body.encode('utf-8')
    msg.attach(MIMEText(body_encoded, 'plain', 'utf-8'))

    # Connect to SMTP server and send email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email, msg.as_string())

@require_POST
def verify_email(request):
    if request.method == 'POST':
        # Process the POST request to verify the email
        # Your verification logic here
        return JsonResponse({"message": "Verification email sent successfully"})
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)
    
def user_logout(request):
    logout(request)        
    return redirect('/custom')


