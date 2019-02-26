from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


# User views.

def register(request):

    """Public users registration form"""

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "You have successfully created an account. Please login")
            return redirect('login')
    else:    
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})



@login_required
def profile(request):

    """account profile update form"""

    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        #check if submitted form is valid and saving
        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            messages.success(request, "Account updated successfully")
            return redirect('profile')
    else:
        user_update_form = UserUpdateForm(instance=request.user)
        profile_update_form = ProfileUpdateForm(instance=request.user.profile)

    context ={
        'user_update_form':user_update_form,
        'profile_update_form':profile_update_form
    }
    return render(request, 'users/profile.html', context)    