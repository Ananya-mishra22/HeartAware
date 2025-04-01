"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from myapp.views import *

  # Import the index view explicitly
  # Import the index view explicitly

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('signup',signup,name='signup'),
    path('login',signin,name='login'),
    path('blogs',blogs,name='blogs'),
    path('contact',contact,name='contact'),
    path('logout',logout_view,name='logout'),
    path('history',history,name='history'),
    path('recommendations',recommendations,name='recommendations'),
    path('symptoms', symptoms, name='symptoms'),
    path('health',health,name='health'),
    path('myths',myths,name='myths'),
    path('personal_stories',personal_stories,name='personal_stories'),
    path('research_innovations',research_innovations,name='research_innovations'),
    path('cardiac_rehab',cardiac_rehab,name='cardiac_rehab'),
    path('2decho', predict_view, name='predict'),
    path('wpr_form', calculate_wpr, name='calculate_wpr'),
    path("lifestyle", predict_heart_attack, name='lifestyle'),
    path('predict/', predict_heart_attack, name='predict_lifestyle'),

]
