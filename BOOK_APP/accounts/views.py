from pickle import NONE
from django.shortcuts import render, redirect
from django.contrib.auth import login as user_login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q


# Create your views here.
def register(request):
    if request.method == "POST":
        # Get value from html template `input name`
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        cpassword = request.POST.get("cpassword")

        # Check the user already exist or not.
        # If exist throw the below error.
        user = User.objects.filter(
            Q(username=username) |
            Q(email=email)
        )
        if user.count() > 0:
            messages.error(request, "Username or Email already exists.")
            return redirect("register")

        if len(password) < 6:
            # If password less than 6, it will show this error, top of the register form
            messages.error(request, "Password must be more than 6 character!")
            return redirect("register")
        if password == cpassword:
            User.objects.create_user(username=username, email=email, password=password)
            # send request to login page.
            return redirect("login")
        else:
            messages.error(request, "Registration failed!")
    return render(request, "register.html")


def login(request):
    if request.method == "POST":
        username = request.POST.get('username',NONE)
        password = request.POST.get('password',NONE)
        # check user already exist or not. if not throw
        # user already exist error.
        user = User.objects.filter(username=username).exists()
        if not user:
            messages.error(request, "User not exist, Please register first")
            return redirect("login")
        # make user authenticated and then send
        # page to task home task list page.
        user = authenticate(username=username, password=password)
        # check user existence, must user exist
        if user is not None:
            user_login(request, user)
            return redirect('task_home')
        else: messages.error(request, "Logged in failed!")
    return render(request, 'login.html')


def logout_view(request):
    # logout & redirect to login page again.
    logout(request)
    return redirect('login')

