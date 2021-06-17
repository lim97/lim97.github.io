from django.urls import path
from . import views
app_name ="trading"

urlpatterns= [path("home/",views.TradingHome,name="home"),]