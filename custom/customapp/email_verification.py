from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import smtplib
import string
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .email_verification import send_verification_email, generate_verification_code  # Assuming the functions are defined in email_verification.py
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
    body = "Your verification code is: " + verification_code
    body_encoded = body.encode('utf-8')
    msg.attach(MIMEText(body_encoded, 'plain', 'utf-8'))

    # Connect to SMTP server and send email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email, msg.as_string())
def generate_verification_code():
    # Generate a random 6-character verification code
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@require_POST
def verify_email(request):
    # You can handle the POST request parameters if needed
    # For example, you might need to get the user's email address from the request

    # Generate verification code
    verification_code = generate_verification_code()

    # Replace 'recipient_email@gmail.com' with the user's email address
    send_verification_email("recipient_email@gmail.com", verification_code)

    # Return a JSON response indicating success
    return JsonResponse({"message": "Verification email sent successfully"})
