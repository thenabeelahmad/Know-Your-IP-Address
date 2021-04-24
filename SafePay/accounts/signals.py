# to collect ip.
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver


# Create your views here.


# def for collecting ip of user

def login_success():

    ip = request.META.get('HTTP_X_FORWARDED_FOR')


    request.session['ip'] = ip
