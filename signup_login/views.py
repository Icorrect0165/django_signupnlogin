from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm, OTPForm
from .models import UserProfile
from .utils import verify_otp  # Assuming you have a utility function to verify OTP 
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.
# def signup(request):
#     return render(request, 'signup.html')

def index(request):
    return render(request, 'index.html')

def login_view(request):
    error_message = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = UserProfile.objects.get(username=username)
                if check_password(password, user.password):
                    # Log the user in manually (store user id in session)
                    request.session['userprofile_id'] = user.id
                    return redirect('index')
                else:
                    error_message = "Invalid username or password."
            except UserProfile.DoesNotExist:
                error_message = "Invalid username or password."
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form, 'error_message': error_message})

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = UserProfile(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                mobile_number=form.cleaned_data['mobile_number'],
                password=make_password(form.cleaned_data['password']),  # Hash the password
            )
            user.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def otp_view(request):
    if request.method == 'POST':
        form = OTPForm(request.POST)
        if form.is_valid():
            otp = form.cleaned_data['otp']
            # Verify the OTP here (e.g., using a third-party service or your own database)
            if verify_otp(otp):
                return redirect('login')
    else:
        form = OTPForm()
    return render(request, 'otp.html', {'form': form})
