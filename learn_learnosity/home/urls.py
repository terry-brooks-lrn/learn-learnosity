from django.urls import include, path
from home import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
]