from datetime import datetime

from django.core.paginator import Paginator
from django.shortcuts import render
from datetime import datetime
from . import models
from django.views.generic import ListView
from .models import Calendars


class CalendarsListView(ListView):

    model = models.Calendars
    paginate_by = 5
    ordering = "created"
    template_name = "calendars/calendars_main.html"
    context_object_name = "calendars"

    def get_queryset(self):
        to_day =datetime.today().day
        to_mon = datetime.today().month
        to_year = str(datetime.today().year)
        if to_mon <10 :
            to_mon = "0"+str(datetime.today().month)
        else :
            to_mon = str(datetime.today().month)
        if to_day < 10:
            to_day = "0" + str(datetime.today().day)
        else:
            to_day = str(datetime.today().day)
        result = to_year + "." + to_mon +"." +to_day
        queryset = Calendars.objects.filter(date=result)
        return queryset

class CalendarsDayView(ListView):
    model = models.Calendars
    paginate_by = 5
    ordering = "created"
    template_name = "calendars/calendars_main.html"
    context_object_name = "calendars"

    def get(self,request,date):

        cal = Calendars.objects.filter(date = date)
        data = {'calendars': cal}
        return render(request, 'calendars/calendars_main.html', data)
