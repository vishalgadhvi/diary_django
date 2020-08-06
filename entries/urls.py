import views as views
from django.urls import path
from . import views


urlpatterns = [
    path("home", views.home,name='home'),
    path("add", views.add,name='add'),
]