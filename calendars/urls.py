from django.urls import path
from . import views

app_name="calendars"

urlpatterns= [path("home/",views.CalendarsListView.as_view(),name="home"),
              path("home/<date>",views.CalendarsDayView.as_view(),name="day"),
              ]