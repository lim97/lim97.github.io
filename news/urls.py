from django.urls import path
from . import views
app_name="news"

urlpatterns = [path("home/",views.NewsHomeView,name="home"),]