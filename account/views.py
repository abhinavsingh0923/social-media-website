from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from .models import *
from django.contrib.auth import authenticate, login, logout
from home.views import index
from django.contrib.auth import login as login_process
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.



# authentication system 

def register(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1== password2:
            user=User.objects.create_user(username=username,email=email,password=password1)
            user.first_name=fname
            user.last_name=lname
            user.save()

            user_login=auth.authenticate(username=username,password=password1)
            auth.login(request,user_login)

            user_model=User.objects.get(username=username)
            new_profile=profile.objects.create(user=user_model,id_username=user_model.id)
            new_profile.save()
            return redirect('editprofile')
        else:
            return render(request,'error.html')    
    return render(request,'account/register.html')   


def handlelogin(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        # print(user)
        if user is not None:
            login_process(request,user)
            return redirect('index')
        else:
            return redirect('error')
    else:
        return render(request,'account/login.html')


def handlelogout(request):
    logout(request)
    return redirect("handlelogin")


# error page loading function 

def error(request):
    return render(request,"error.html")



# @login_re
# def editprofile(request):
#     user_profile=profile.objects.get(user=request.user)

#     if request.method=="POST":
#         if request.FILES.get['profilephoto']!=None:
#             user_profile.profile_photo=request.FILES['profilephoto']
#             user_profile.bio=request.POST['bio']
#             user_profile.location=request.POST['location']
#             user_profile.save()
#             return redirect('index')
       
#     else:
#         # return render(request,'error.html')    
#         return render (request,'home/editprofile.html')

@login_required
def editprofile(request):
    user_profile = profile.objects.get(user=request.user)

    if request.method == 'POST':
        
        if request.FILES.get('profilephoto') == None:
            image = user_profile.profilephoto
            bio = request.POST['bio']
            location = request.POST['location']

            user_profile.profile_photo = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
        if request.FILES.get('profilephoto') != None:
            image = request.FILES.get('profilephoto')
            bio = request.POST['bio']
            location = request.POST['location']

            user_profile.profile_photo = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
        
        return redirect('editprofile')
    return render(request, 'home/editprofile.html', {'user_profile': user_profile})        
