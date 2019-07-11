from django.conf.urls import url
from . import views
from django.views.generic import  ListView, DetailView
from  .models import  Profile


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'search$', views.search)
    #url(r'search$', ListView.as_view(queryset=Profile.objects.order_by('subjectName'),template_name='vapp/searchres.html'))
]