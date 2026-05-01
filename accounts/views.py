from itertools import chain
from django.core.paginator import Paginator
from django.shortcuts import render,redirect,get_object_or_404
from urllib3 import request
from .models import Profile
from blog.models import Documentry,Food,Travel,News,Story
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup_page(request):
    error=''
    if request.method == 'POST':
        a=request.POST
        name=a.get('name')
        email=a.get('email')
        password=a.get('password')
        password2=a.get('password2')
        image=request.FILES.get('image')
        
        if User.objects.filter(username=name).exists():
            error='Username already exists'
        elif not name:
            error='Please enter a username'
        elif not email:
            error='Please enter an email'
        elif User.objects.filter(email=email).exists():
            error='Email already exists'
        elif password != password2:
            error='Passwords do not match'
        else:
            user = User.objects.create_user(username=name, email=email, password=password)
            Profile.objects.create(user=user, image=image)
            return redirect('login')
    return render(request, 'auth/signup.html', {'error': error})

def login_page(request):
    if request.method == 'POST':
        a=request.POST
        name=a.get('name')
        password=a.get('password')
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'auth/login.html', {'error': 'Invalid username or password'})
    return render(request, 'auth/login.html')
@login_required
def profile_page(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    
    return render(request, 'auth/user_dasboard.html',)
def logout_page(request):
    logout(request)
    return redirect('login')
@login_required
def update_profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method == 'POST':
            a=request.POST
            name=a.get('name')
            email=a.get('email')
            image=request.FILES.get('image')
            
            user = request.user
            user.username = name
            user.email = email
            user.save()
            
            profile = user.profile
            if image:
                profile.image = image
                profile.save()
            
            return redirect('profile')
    return render(request, 'auth/signup.html')
@login_required
def Edit_bio(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method == 'POST':
            bio_text = request.POST.get('bio')
            profile, created = Profile.objects.get_or_create(user=request.user)
            profile.bio = bio_text
            profile.save()
            
            return redirect('profile')
    return render(request,'auth/edit_bio.html')
@login_required
def My_posts(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        docomentry = Documentry.objects.filter(User_relation=request.user)
        food = Food.objects.filter(User_relation=request.user)
        travel = Travel.objects.filter(User_relation=request.user)
        news = News.objects.filter(User_relation=request.user)
        story = Story.objects.filter(User_relation=request.user)
        posts=sorted(chain(docomentry , food , travel , news , story), key=lambda x: x.created_at, reverse=True)
        paginator = Paginator(posts, 6)
        page_number = request.GET.get('page')
        posts = paginator.get_page(page_number)
    return render(request,'auth/my_posts.html', {'posts': posts,'post':posts})
@login_required
def add_post(request):
    error=''
    if not request.user.is_authenticated:
        return redirect('login')
    
    else:
        
        if request.method == 'POST':
            title = request.POST.get('title')
            category = request.POST.get('category')
            description = request.POST.get('description')
            image = request.FILES.get('image')
            
            if category == 'Documentry':
                Documentry.objects.create(title=title, category=category, description=description, image=image, User_relation=request.user)
            elif category == 'Story':
                Story.objects.create(title=title, category=category, description=description, image=image, User_relation=request.user)
            elif category == 'Food':
                Food.objects.create(title=title, category=category, description=description, image=image, User_relation=request.user)
            elif category == 'Travel':
                Travel.objects.create(title=title, category=category, description=description, image=image, User_relation=request.user)
            elif category == 'News':
                News.objects.create(title=title, category=category, description=description, image=image, User_relation=request.user)
            elif not title:
                error='Please enter a title'
            elif not category:
                error='Please select a category'
            elif not description:
                error='Please enter a description'
            elif not image:
                error='Please upload an image'
            else:
                error='Your post has been published'
                
            
            return redirect('my_posts')
    return render(request,'auth/add_posts.html', {'error': error})

def update_post(request, category, id):

    doc1 = None
    if request.method == 'GET':

        if category == 'Documentry':
            doc1 = Documentry.objects.get(id=id)
        elif category == 'Story':
            doc1 = Story.objects.get(id=id)
        elif category == 'Food':
            doc1 = Food.objects.get(id=id)
        elif category == 'Travel':
            doc1 = Travel.objects.get(id=id)
        elif category == 'News':
            doc1 = News.objects.get(id=id)

        return render(request, 'auth/add_posts.html', {'doc': doc1})
    if request.method == 'POST':

        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        if category == 'Documentry':
            doc1 = Documentry.objects.get(id=id)
        elif category == 'Story':
            doc1 = Story.objects.get(id=id)
        elif category == 'Food':
            doc1 = Food.objects.get(id=id)
        elif category == 'Travel':
            doc1 = Travel.objects.get(id=id)
        elif category == 'News':
            doc1 = News.objects.get(id=id)
        doc1.title = title
        doc1.description = description

        if image:
            doc1.image = image

        doc1.User_relation = request.user
        doc1.save()

        return redirect('my_posts')
    
def delete_post(request,category,id):
    if category=='Documentry':
        post=Documentry.objects.get(id=id)
    elif category == 'Story':
        post = Story.objects.get(id=id)
    elif category == 'Food':
        post = Food.objects.get(id=id)
    elif category == 'Travel':
        post = Travel.objects.get(id=id)
    elif category == 'News':
        post = News.objects.get(id=id)
    if post:
        post.delete()
        return redirect('my_posts')


        

    
