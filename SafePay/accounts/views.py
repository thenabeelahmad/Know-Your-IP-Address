from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

# # to collect ip.
# from django.contrib.auth.signals import user_logged_in
# from django.contrib.auth.models import User
# from django.dispatch import receiver




# # Create your views here.


# # def for collecting ip of user

# @receiver(user_logged_in, sender=User)
# def login_success(sender,request,user, **kwargs):
#     ip = request.MTA.get('REMOTE_ADDR')
#     request.session['ip'] = ip

def home(request):
    ip = request.session.get('ip',0)
    return render(request,'home.html',{'ip':ip})


def studash(request):
    return render(request,'studentdashboard.html')

# admin login code
def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    # admin check
    if user.is_authenticated and user.is_superuser:
      auth.login(request, user)
      return redirect('home')
    else:
      return redirect('badcredit')
  else:
    return render(request, 'login.html')


# student login code

def stulogin(request):
  if request.method == 'POST':
    username = request.POST['stuid']
    password = request.POST['stupass']

    user = auth.authenticate(username=username, password=password)

    # check for non superuser
    if user.is_authenticated and not user.is_superuser:
      auth.login(request, user)
      messages.error(request, 'Please come again')
      return redirect('studash')
    else:
      return redirect('badcredit')
  else:
    return render(request, 'stulogin.html')


# if user tries to login from wrong role
def badcredit(request):
    return render(request,'badcredit.html')


# sign up

def register(request):
  if request.method == 'POST':
    # Get form values
    username = request.POST['username']
    password = request.POST['password']
    password2 = request.POST['password2']

    # Check if passwords match
    if password == password2:
      # Check username
      if User.objects.filter(username=username).exists():
        messages.error(request, 'That username exists')
        return redirect('register')
      else:
        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, 'Student now registered and can log in')
        return redirect('register')
    else:
      messages.error(request, 'Passwords do not match')
      return redirect('register')
  else:
    return render(request, 'accounts/register.html')


def logout(request):
  if request.method == 'POST':
    print(1)
    auth.logout(request)
    print(1)
    return redirect('login')
  else:
    auth.logout(request)
    return redirect('login')