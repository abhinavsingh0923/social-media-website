from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from .models import post,likepost,followercount
from account.models import profile
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    allpost=post.objects.all()
    params={'allposts':allpost}
    return render(request,'home/home.html',params)
    
# def chatting(request):
#     return render(request,'chat/chatting.html')
    
@login_required    
def profilepage(request):
    user_obj=User.objects.get(username=request.user.username)
    profile_obj=profile.objects.get(user=user_obj)
    user_post=post.objects.filter(user=request.user.username)
    user_post_length=len(user_post)
    user_followers = len(followercount.objects.filter(user=request.user.username))
    user_following = len(followercount.objects.filter(follower=request.user.username))
    params={
        'profile_obj':profile_obj,
        'user_post':user_post,
        'user_post_length':user_post_length,
        'user_followers': user_followers,
        'user_following': user_following,
        }
    return render(request,'home/profilepage.html',params)




@login_required    
def addpostfunction(request):
    if request.method == 'POST':
        user=request.user.username
        image=request.FILES.get('image')
        caption=request.POST['caption']
        newpost=post(user=user,image=image,caption=caption)
        newpost.save()
        return redirect('index')
    else:    
        return render(request,'home/addpost.html')

@login_required
def like_post(request):
    username=request.user.username
    post_id= request.GET.get('post_id')
    
    posts= post.objects.get(id=post_id)

    like_filter=likepost.objects.filter(post_id=post_id,username=username).first()

    if like_filter==None:
        new_like= likepost(post_id=post_id,username=username)
        new_like.save()
        posts.no_of_likes=posts.no_of_likes+1
        posts.save()
        return redirect('index')
    else:
        like_filter.delete()
        posts.no_of_likes=posts.no_of_likes-1
        posts.save()
        return redirect('index')


@login_required
def search(request):
    if request.method=='POST':
        username = request.POST['username']
        user_obj=User.objects.get(username=username)
        if user_obj is not None:
            username_object = profile.objects.filter(user=user_obj)
            print(username_object)
            params={'username_object': username_object}
            return render(request,'home/search.html',params)
        else:
            return render(request,'error.html')    
    else:
        return render(request, 'home/search.html')


@login_required
def otherprofilepage(request,pk):
    user_obj=User.objects.get(username=pk)
    user_profile=profile.objects.get(user=user_obj)
    user_post=post.objects.filter(user=pk)
    user_post_length=len(user_post)

    follower = request.user.username
    user = pk

    if followercount.objects.filter(follower=follower, user=user).first():
        button_text = 'Unfollow'
    else:
        button_text = 'Follow'

    user_followers = len(followercount.objects.filter(user=pk))
    user_following = len(followercount.objects.filter(follower=pk))

    context={
        'user_obj':user_obj,
        'user_profile':user_profile,
        'user_post':user_post,
        'user_post_length':user_post_length,
        'button_text': button_text,
        'user_followers': user_followers,
        'user_following': user_following,
    }


    return render(request,'home/otherprofilepage.html',context)




@login_required
def follow(request):
    if request.method=="POST":
        follower=request.POST['follower']
        user=request.POST['user']

        if followercount.objects.filter(follower=follower,user=user).first():
            delete_follower=followercount.objects.get(follower=follower,user=user)
            delete_follower.delete()
            return redirect('/home/otherprofilepage/'+user)
        else:
            new_follower=followercount.objects.create(follower=follower,user=user)
            new_follower.save()
            return redirect('/home/otherprofilepage/'+user)

    else:
        return redirect('index')    


