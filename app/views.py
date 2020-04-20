"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.conf import settings
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact Me',
            'year':datetime.now().year,
        }
    )

def success(request):
    """Renders the successful registration page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/success.html',
        {
            'title':'Success',
            'message':'Registration Successul.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About This Web-Application',
            'year':datetime.now().year,
        }
    )

def login(request, user):
    """Renders the login page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/login.html',
        {
            'title':'Login',
            'message':'Enter login credentials here.',
            'year':datetime.now().year,
        }
    )


def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'app/register.html', {'title':'Register', 'year':datetime.now().year, 'form': form})


def regsuccess(request):
    """ Check if user is authenticated or not. If not, kick back to homepage."""
    if request.user.is_authenticated:
        """Renders the successful registration page."""
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/success.html',
            {
                'title':'User Authentication Completed',
                'message':'Viewing Authenticated Web Page',
                'year':datetime.now().year,
            }
    )
    else:
        return redirect('home')
