from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='index'),
    url(r'^post/(?P<slug>[\w-]+)/$', views.post_detail, name='post_detail'),
    url(r'^oauth/disconnect/facebook/$', views.logout, name='logout'),
    url(r'^macapps/$', views.listapps, name='list_apps'),
    url(r'^macapps/(?P<slug>\S+)/$', views.appdetail, name='app_detail'),
    url(r'^test/$', views.testAutoComplete, name='testautocomplete'),
    url(r'^search/', views.search, name='search'),
]