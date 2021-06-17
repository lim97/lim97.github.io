from django.urls import path
from lns import views as lns_view
app_name="lns"

urlpatterns = [path("home/",lns_view.main,name="home"),]