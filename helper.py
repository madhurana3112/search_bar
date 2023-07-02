import random
import re
from django.core.mail import send_mail
from django.conf import settings

def validate_email(email):
    """If email entered is correct or not"""
    regex= r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if(re.fullmatch(regex, email)):
        return True
    return False

def generate_otp():
    """Generates 6 digit otp"""
    return random.randrange(100000,999999)

def send_otp(user,otp):
    subject = 'Welcome to Search website '
    message = f'Hi {user.first_name}, Your Verification otp is {otp}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email,]
    send_mail( subject, message, email_from, recipient_list )
