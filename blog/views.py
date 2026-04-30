from django.http import JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from .models import Documentry, Story, Food, Travel, News,comment
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    query = request.GET.get('q', '')
    data = {
        'documentries': Documentry.objects.order_by('-created_at')[:5],
        'stories': Story.objects.order_by('-created_at')[:5],
        'foods': Food.objects.order_by('-created_at')[:5],
        'travels': Travel.objects.order_by('-created_at')[:5],
        'news': News.objects.order_by('-created_at')[:5],
        'documentry':query,
        
    }
        
    if query:
        data['documentries'] = Documentry.objects.filter(title__icontains=query).order_by('-created_at')
        data['stories'] = Story.objects.filter(title__icontains=query).order_by('-created_at')
        data['foods'] = Food.objects.filter(title__icontains=query).order_by('-created_at')
        data['travels'] = Travel.objects.filter(title__icontains=query).order_by('-created_at')
        data['news'] = News.objects.filter(title__icontains=query).order_by('-created_at')
    
        
    return render(request, 'home.html', data)

def detail_page(request,category, id):
    data={
         'documentry':Documentry,
            'story':Story,
            'food':Food,
            'travel':Travel,
            'news':News
    }
    category = category.lower()
    get_obj=data.get(category)
    related_objs=get_obj.objects.order_by('-created_at')[:3]
    
    obj=get_object_or_404(get_obj, id=id)
    data1={
         'documentry':'d_relation',
            'story':'s_relation',
            'food':'f_relation',
            'travel':'t_relation',
            'news':'n_relation'
    }
    
    if request.method=='POST':
        comment1=request.POST.get('comment')
        if comment1:
            save_commment=comment(
             User_relation=request.user,
            content=comment1,

            )
            obj1=data1.get(category.lower())
            setattr(save_commment, obj1, obj)
            save_commment.save()
            return JsonResponse({'message': 'Comment submitted successfully!'})
    obj1=data1.get(category.lower())
    comments=comment.objects.filter(**{obj1: obj}).order_by('-created_at')[:3]
    
        

    return render(request, 'view_detail_page.html', {'obj': obj, 'related_objs': related_objs, 'comments': comments})


def documentry(request):
    documentry=Documentry.objects.all().order_by('-created_at')
    paginator = Paginator(documentry, 6)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'documentry_page.html', {'posts':posts})

def story(request):
    stories = Story.objects.order_by('-created_at')
    paginator = Paginator(stories, 6)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'story_page.html', {'posts': posts})

def food(request):
    foods = Food.objects.order_by('-created_at')
    paginator = Paginator(foods, 6)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'food_page.html', {'posts': posts})

def travel(request):
    travels = Travel.objects.order_by('-created_at')
    paginator = Paginator(travels, 6)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'traval_page.html', {'posts': posts})

def news(request):
    news = News.objects.order_by('-created_at')
    paginator = Paginator(news, 6)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'News.html', {'posts': posts})