from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You can log in now')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        us_form = UserUpdateForm(request.POST, instance=request.user)
        pf_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if us_form.is_valid() and pf_form.is_valid():
            us_form.save()
            pf_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        us_form = UserUpdateForm(instance=request.user)
        pf_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'us_form': us_form,
        'pf_form': pf_form
    }
    return render(request, 'users/profile.html', context)

# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error