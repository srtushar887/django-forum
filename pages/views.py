from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import auth
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.db.models import Count
from django.contrib.auth.models import User
from category.models import Post,Category


def index(request):
    posts = Post.objects.order_by('pk').reverse()
    category = Category.objects.annotate(num_posts = Count('post'))
    paginator = Paginator(posts,5)
    page = request.GET.get('page')
    page_posts = paginator.get_page(page)
    context = {
        'posts' : page_posts,
        'category' : category
    }
    return render(request,'pages/home.html',context)

def create_post(request):
    if not request.user.is_authenticated:
        return redirect('loginuser')
    else:
        category = Category.objects.all()
        context = {
            'category' : category
        }
        return render(request, 'pages/createPost.html',context)

def save_user_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        cat = request.POST['catdat']
        des = request.POST['des']
        userid = request.POST['userid']
        cat_tem = get_object_or_404(Category,pk=cat)
        user_id = get_object_or_404(User,pk=userid)
        post = Post.objects.create(title=title,des=des,category=cat_tem,user=user_id)
        post.save()
        return redirect('/')

def porst_details(request, post_id):
    post = get_object_or_404(Post,pk=post_id)
    category = Category.objects.order_by('pk').reverse()
    context = {
        'post' : post,
        'category' : category
    }
    return render(request,'pages/postDetails.html',context)

