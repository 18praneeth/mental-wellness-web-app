from users.views import my_login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):

    context = {
        'title': 'HOME'
    }
    return render(request, 'webpages/home.html', context=context)

