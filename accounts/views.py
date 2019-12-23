from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User

from .models import Profile

def register(request):
    if request.method == 'POST':
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        username = request.POST['user_name']
        email = request.POST['email']
        pass1 = request.POST['pass']
        pass2 = request.POST['pass2']
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username Already Exist')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email Already Exist')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=fname,last_name=lname,username=username,email=email,password=pass1)
                user.save();
                user_id = get_object_or_404(User,pk=user.id)
                Profile.objects.create(user=user_id,image="https://pngimage.net/wp-content/uploads/2018/05/default-user-profile-image-png-2.png")
                messages.success(request, 'Account Created . Please Login !')
                return redirect('loginUser')
        else:
            messages.error(request, 'Password Not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Email or Password not match. Please try again !')
            return redirect('loginUser')
    else:
        return render(request,'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/')

def my_profile(request):
    current_user = request.user.id

    if request.method == 'POST':
       user_id = get_object_or_404(User,pk=current_user)
       fname = request.POST['first_name']
       lname = request.POST['last_name']
       username = request.POST['username']
       email = request.POST['email']
       file = request.FILES['profile_image']
       exist_image = Profile.objects.filter(user=current_user)
       if exist_image.exists():

           user = get_object_or_404(User,pk=current_user)
           user = User.objects.get(pk=user.id)
           user.first_name = fname
           user.last_name = lname
           user.username = username
           user.email = email
           user.save()



           image = get_object_or_404(Profile,user=current_user)

           image.image = file
           image.save()
           return redirect('my_profile')
       else:
           image = Profile.objects.create(user=user_id,image=file)
           image.save()
           return redirect('my_profile')

    else:

        get_user_data = get_object_or_404(User,pk=current_user)
        image = get_object_or_404(Profile,user=current_user)
        context = {
            'user' : get_user_data,
            'image' : image

        }
        return render(request,'accounts/profile.html',context)