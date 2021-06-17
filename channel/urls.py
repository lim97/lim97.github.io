from django.urls import path
from . import views

app_name ="channel"

urlpatterns=[path("home/",views.ChannelHomeView.as_view(),name="home"),
             path("trade/",views.ChannelTradeView.as_view(),name="trade"),
             path("youtube/",views.ChannelYoutubeView.as_view(),name="youtube"),
             path("kakao/",views.ChannelKakaoView.as_view(),name="kakao"),
             path("etc/", views.ChanneletcView.as_view(), name="etc"),
             ]