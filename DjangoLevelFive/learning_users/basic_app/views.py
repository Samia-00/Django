# basic_app/views.py
from django.shortcuts import render, redirect
from basic_app.forms import UserProfileInfoForm, UserForm
from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponseRedirect, HttpResponse
# from django.core.urlresolvers import reverse
from django.urls import reverse
# from django_scrypt.hashers import ScryptPasswordHasher
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request, 'basic_app/index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!!!!")

@login_required
def user_logout(request):
    logout(request)
    return render(request, 'basic_app/index.html')
    # return HttpResponseRedirect(reverse('basic_app:index.html'))

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            password = user_form.cleaned_data['password']
            user.set_password(password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
            login(request, user)  # Automatically log the user in upon registration
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'basic_app/registration.html',
                    {'user_form': user_form,'profile_form': profile_form,'registered': registered})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect('index')  # Use the 'index' named URL to redirect
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to log in and failed!!!")
            print("Username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details supplied!!")
    else:
        return render(request, 'basic_app/login.html', {})