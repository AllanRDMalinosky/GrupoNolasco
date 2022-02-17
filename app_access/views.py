from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import date


# import formularios


# Create your views here.


def login(request):

    return render(
        request,
        "login.html",
    )


def redirecionamento(request):
    return redirect("/app_access/login")
