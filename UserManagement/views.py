from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile

# Create your views here.

def register(request):
    #creating an empty form for user registration
    form = UserCreationForm()

    # after submit button in the HTML page
    if request.method == "POST":
        # filling out the form with the inserted data from HTML page
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # if valid then save to database
            form.save()
            # after a successful registration you can redirect to any page
            return redirect('home')

    context={
        'form' : form
    }

    return render(request, 'UserManagement/register.html', context)



@login_required
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



@login_required
def show_profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = "Please complete your profile to view"

    context ={
        'profile' : profile
    }
    
    return render(request, 'UserManagement/show_profile.html', context)