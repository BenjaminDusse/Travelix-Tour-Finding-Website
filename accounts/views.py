from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

from accounts.forms import UserRegisterForm


def Register(request):
    if request.method == 'POST':
        reg_form = UserRegisterForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            # htmly = get_template('accounts/email.html')
            # d = {'username': username}
            # subject, from_email, to = 'welcome', 'abduhakimovfazliddin2002@gmail.com', email
            # html_content = html.render(d)
            # msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            # msg.attach_alternative(html_content, "text/html")
            # msg.send()

            messages.success(request, f"Your account has been created! You are now able to log in.")
            return redirect('accounts:login')

    else:
        reg_form = UserRegisterForm()

    context = {
        'register_form': reg_form,
        'title': 'Register Here'
    }
    return render(request, 'accounts/register.html', context)


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            log_form = login(request, user)
            messages.success(request, f'Welcome {username}')
            return redirect('travelix:home')
        else:
            messages.info(request, f'Account does not exist')
    log_form = AuthenticationForm()

    context = {
        'log_form': log_form,
        'title': 'Log In'
    }
    return render(request, 'accounts/login.html', context)

