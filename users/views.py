from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from training.models import TrainingEvent


# Django templates
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f' {username} your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()

    
    return render(request, 'users/register.html',{'form':form})

# only when they are logged in, show form to update name user and image

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm( request.POST,
                                    request.FILES,
                                    instance= request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm( instance= request.user.profile)

    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, 'users/profile.html', context)

# API
# from rest_framework.decorators import api_view
# from django.http import JsonResponse
# from django.contrib.auth import login
# from django.contrib.auth import authenticate


# @api_view(['POST'])
# def api_login(request):
#     username = request.data.get('username')
#     password = request.data.get('password')
#     print(request.data)
#     user = authenticate(username=username, password=password) 
#     if user is not None:
#         login(request, user)
#         return JsonResponse({'message': 'Login successful'}, status=200)
#     else:
#         return JsonResponse({'message': 'Invalid credentials'}, status=400)



