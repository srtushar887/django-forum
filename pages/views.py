from django.shortcuts import render,redirect,get_object_or_404

from category.models import Post,Category
def index(request):
    return render(request,'pages/home.html')

def create_post(request):
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
        cat_tem = get_object_or_404(Category,pk=cat)
        post = Post.objects.create(title=title,des=des,category=cat_tem)
        post.save()
        return redirect('/')

