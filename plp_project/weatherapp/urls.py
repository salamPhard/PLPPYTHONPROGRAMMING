from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home"),
    #path("city/", views.check_data, name="search")

]
