from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, ChatForm
from .models import Profile, Chat
from django.core.mail import send_mail
import random
import string

from ProductManagement.models import Cart

v_code = '123'

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
            user = form.save()

            # create a new cart for new user
            cart = Cart(user = user)
            cart.save()

            # after a successful registration you can redirect to any page
            return redirect('products_list')

    context={
        'form' : form
    }

    return render(request, 'UserManagement/register.html', context)



@login_required
def create_profile(request):


    profile_list = Profile.objects.filter(user=request.user)

    if len(profile_list) != 0:
        profile = Profile.objects.get(user=request.user)
        form = ProfileForm(initial={'contact_no': profile.contact_no,
                                    'mobile_no': profile.mobile_no,
                                    'portfolio_url': profile.portfolio_url,
                                    'cv': profile.cv,
                                    })
    else:
        profile = None
        form = ProfileForm()


    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid:
            instance = form.save(commit=False)
            instance.user = request.user

            #instance.save()

            if profile == None:
                instance.save()
            else:
                profile.contact_no = instance.contact_no
                profile.pro_pic = instance.pro_pic
                profile.save()

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


def id_generator(size=16, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


@login_required
def send_email(request):
    recipient_list = []
    subject = ''
    message = ''
    status = Profile.objects.get(user=request.user).status
    user_message = '' + status

    if request.method == 'POST':

        recipient_list.append( request.POST['recipient'] )
        subject = request.POST['subject']

        code = id_generator()
        v_code = code
        request.session['v_code'] = code

        message += request.POST['body']
        message += '\n Activation code: ' + code


        status = send_mail(
            subject = subject,
            message = message,
            from_email = 'contact.formulabd71@gmail.com',
            recipient_list = recipient_list,
            fail_silently = True
        )

        if status == 1:

            user_message = 'Email sent successfully. Please enter the verification code.'
            context = {
                'message': user_message
            }

            return redirect('verification')
        else:
            user_message = 'Failed! Try again please!'

    context = {
        'message' : user_message
    }
    return render(request, 'UserManagement/send_email.html', context)



@login_required
def verify_email(request):
    message = ''

    if request.method == "POST":
        code = request.POST['code']
        print(code, request.session['v_code'])
        message = 'Not matched!'

        if request.session['v_code'] == code:
            message = "Successful! Your account if activated now!"
            profile = Profile.objects.get(user = request.user)
            profile.status = "True"
            profile.save()
            context = {
                'message': message
            }
            return render(request, 'UserManagement/success.html', context)

    context = {
        'message': message
    }
    return render(request, 'UserManagement/email_verification_code.html', context)

@login_required
def send_message(request):
    form = ChatForm()

    all_messages = Chat.objects.filter(receiver=request.user)

    if request.method == "POST":
        form = ChatForm(request.POST, request.FILES)

        if form.is_valid:
            instance = form.save(commit=False)
            instance.sender = request.user
            instance.save()


    context = {
        'form' : form,
        'all_messages': all_messages
    }

    return render(request, 'UserManagement/Chat.html', context)


def save_profile_session(request):

    if request.user.is_authenticated:
        profile_list = Profile.objects.filter(user = request.user)

        if( len(profile_list) != 0 ):
            request.session['profile_pic'] = profile_list[0].pro_pic.url

    return redirect('products_list')

def abouts(request):
    return render(request, 'UserManagement/about.html')
