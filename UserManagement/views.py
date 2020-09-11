from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm
from .models import Profile

# Create your views here.

def register(request):
    form = UserCreationForm()
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={
        'form' : form
    }

    return render(request, 'UserManagement/register.html', context)



def create_profile(request):
    form = ProfileForm()

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid:
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()

            return redirect('products_list')

    context = {
        'form' : form
    }
    return render(request, 'UserManagement/create_profile.html', context)


def show_profile(request):
    #profile = Profile.objects.get(user=request.user)

    #profile = get_object_or_404(Profile, user=request.user)
    profile = "Please complete your profile to view"

    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = "Please complete your profile to view"

    context ={
        'profile' : profile
    }
    
    return render(request, 'UserManagement/show_profile.html', context)