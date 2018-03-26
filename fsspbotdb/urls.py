from django.conf.urls import url,include 
from django.urls import  path,re_path
from . import views
from fsspbotdb.views import  *
urlpatterns = [
    path("", views.index, name='index'),
    path("set_webhook", views.set_webhook, name='set_webhook'),
    path("HOOK", views.webhook, name='webhook'),
    #path("<slug:slug>", views.webhook, name='webhook'),
    
    
    
]
