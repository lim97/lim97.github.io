from math import ceil
from django.shortcuts import render
from . import models
def NewsHomeView(request):
    page = request.GET.get("page", 1)
    page = int(page or 1)
    page_size = 2
    limit = page_size * page
    offset = limit - page_size
    all_news = models.News.objects.all()[offset:limit]
    page_count = ceil(models.News.objects.count() / page_size)
    return render(
        request,
        "news/news_list.html",
        {
            "all_news": all_news,
            "page": page,
            "page_count": page_count,
            "page_range": range(1, ceil(page_count + 1)),
        },
    )



