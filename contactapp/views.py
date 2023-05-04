from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth import views as auth_views
from django.contrib import messages
from .models import student_forms
# student = student_form()
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def contact_view(request):
    if request.method == 'POST':
        # Handle contact form submission
         
        messages.success(request, 'Your message has been sent. Thank you!')
        return render(request,"home.html",{'form':student_forms})  
                
    else:
        # Display contact form
        return render(request, 'contact.html')

def home(request):
    return render(request, 'home.html', {})

def menu_view(request):
    logout(request)
    return render(request, 'menu.html',{})

