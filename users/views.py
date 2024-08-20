from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    context = {
        'form': form,
    }
    return render(request, 'users/signup.html', context)

def login(request):
    # if request.user.is_authenticated:
    #     return redirect('index')  # Redirect to the home page if the user is already authenticated

    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next')
                return redirect(next_url if next_url else 'index')  # Redirect to 'next' URL or home page
            else:
                messages.error(request, 'Login unsuccessful. Check email and password!')

    else:
        form = LoginForm()

    return render(request, 'users/login.html', {'form': form, 'title': 'Login'})

#   Login page
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST or None, instance=request.user)

        p_form = ProfileUpdateForm(request.POST or None,  request.FILES, instance=request.user.profilemodel)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profilemodel)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile.html', context)

#   Logout route
@login_required
def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('logout_success')
    return render(request, 'users/logout.html')

def logout_success(request):
    return render(request, 'users/logout_success.html')

    