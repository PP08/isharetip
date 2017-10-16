from django.shortcuts import render
from .models import Post, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    all_post = Post.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(all_post, 4)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'mactip/index.html', {'posts': posts, 'node': 'Home page'})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    category = post.category
    node = 'Post / ' + str(category)
    # node = "POST"
    return render(request, 'mactip/post_detail.html', {"post": post, 'node': node})
