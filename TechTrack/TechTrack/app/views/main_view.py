from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.conf import settings
from django.template import loader
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logou
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordResetForm
from django.db.models.query_utils import Q
from django.core.mail import send_mail

import os
import sys

def login(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        return render(request, 'login.html', {})

@login_required
def homepage(request):
    return render(request,'TechTrack-Page2.html',{})

@login_required
def logout(request):
    auth_logout(request)
    return redirect('login_user')
