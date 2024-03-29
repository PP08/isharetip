from django.shortcuts import render, redirect
from .models import Post, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import logout as auth_logout
from pymongo import MongoClient
import pymongo
import re

client = MongoClient("mongo", 27017)
db = client.database
table = db.macapps

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

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    category = post.category
    node = 'Post / ' + str(category)
    # node = "POST"
    return render(request, 'mactip/post_detail.html', {"post": post, 'node': node})

def logout(request):
    """Logs out user"""
    next = request.GET['next']
    auth_logout(request)
    return redirect(next)

def listapps(request):
    ''''''
    # apps = list(table.find().limit(30))
    # return render(request, 'mactip/listapps.html', {"apps": apps})
    all_apps = list(table.find().sort('date_upload', pymongo.DESCENDING))
    try:
        page = request.GET.get('page', 1)
        paginator = Paginator(all_apps, 12)
        apps = paginator.page(page)
    except PageNotAnInteger:
        apps = paginator.page(1)
    except EmptyPage:
        apps = paginator.page(paginator.num_pages)
    return render(request, 'mactip/listapps.html', {'apps': apps, 'node': 'Apps'})

def appdetail(request, slug):
    ''''''
    app = dict(table.find_one({"slug": slug}))
    print(app)

    return render(request, 'mactip/appdetail.html', {"app": app, 'node': 'Apps'})

def testAutoComplete(request):
    return render(request, 'mactip/autocomplete.html')

def search(request):
    appname = request.GET["appname"]
    reg = re.compile(r'.*{}.*'.format(appname), re.I)
    all_apps = list(table.find({"name": {"$regex" : reg}}).sort('date_upload', pymongo.DESCENDING))
    try:
        page = request.GET.get('page', 1)
        paginator = Paginator(all_apps, 12)
        apps = paginator.page(page)
    except PageNotAnInteger:
        apps = paginator.page(1)
    except EmptyPage:
        apps = paginator.page(paginator.num_pages)
    return render(request, 'mactip/listapps.html', {'apps': apps, 'node': 'Apps'})

def category(request, category):
    ''''''
    if '-' in str(category):
        original_category = str(category).replace('-', ' ')
    else:
        original_category = str(category)
    all_apps = list(table.find({"category": original_category}).sort('date_upload', pymongo.DESCENDING))
    try:
        page = request.GET.get('page', 1)
        paginator = Paginator(all_apps, 12)
        apps = paginator.page(page)
    except PageNotAnInteger:
        apps = paginator.page(1)
    except EmptyPage:
        apps = paginator.page(paginator.num_pages)
    return render(request, 'mactip/listapps.html', {'apps': apps, 'node': original_category})