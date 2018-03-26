from django.conf.urls import url,include 
from django.urls import  path,re_path
from . import views
from fsspbotdb.views import  *
urlpatterns = [
    path("", views.index, name='index'),
    path("<slug:slug>", views.webhook, name='webhook'),
    
    
    
]
