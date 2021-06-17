from django.urls import path
from home import  views as home_view
from trading import views as trading_view

app_name = "home"

urlpatterns =[path("",trading_view.TradingHome,name ="home")]
