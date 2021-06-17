import paginator
from django.contrib import messages
from django.shortcuts import render
from django.views.generic import  ListView
from . import models
from django.core.paginator import Paginator

# Create your views here.
from .models import Channel, ChannelType


class ChannelHomeView(ListView):

    model = models.Channel
    paginate_by = 10
    ordering = "created"
    template_name = "channel/channel_main.html"
    context_object_name = "channels"

class ChannelTradeView(ListView):

    model = models.Channel
    paginate_by = 10
    ordering = "created"
    template_name = "channel/channel_main.html"
    context_object_name = "channels"
    def get_queryset(self):

        ch1 = ChannelType.objects.get(name = '거래소' )
        queryset = Channel.objects.filter(channeltype = ch1)

        return queryset
class ChannelYoutubeView(ListView):

    model = models.Channel
    paginate_by = 10
    ordering = "created"
    template_name = "channel/channel_main.html"
    context_object_name = "channels"
    def get_queryset(self):

        ch1 = ChannelType.objects.get(name = '유튜브' )
        queryset = Channel.objects.filter(channeltype = ch1)

        return queryset
class ChannelKakaoView(ListView):

    model = models.Channel
    paginate_by = 10
    ordering = "created"
    template_name = "channel/channel_main.html"
    context_object_name = "channels"
    def get_queryset(self):

        ch1 = ChannelType.objects.get(name = '오픈채팅방' )
        queryset = Channel.objects.filter(channeltype = ch1)

        return queryset
class ChanneletcView(ListView):

    model = models.Channel
    paginate_by = 10
    ordering = "created"
    template_name = "channel/channel_main.html"
    context_object_name = "channels"
    def get_queryset(self):

        ch1 = ChannelType.objects.get(name = '기타' )
        queryset = Channel.objects.filter(channeltype = ch1)

        return queryset

