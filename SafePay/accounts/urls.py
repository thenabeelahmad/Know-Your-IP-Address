from django.urls import path
from . import views




urlpatterns = [
    path('', views.login, name='login'),
    path('studentlogin', views.stulogin, name='stulogin'),

    path('Student/Dashboard',views.studash,name="studash"),

    path('Admin/Dashboard',views.home,name="home"),
    path('logout', views.logout, name='logout'),
    path('register', views.register,name='register'),
    path('badcredit',views.badcredit, name="badcredit"),

]