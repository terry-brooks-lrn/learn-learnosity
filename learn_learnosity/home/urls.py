from django.urls import include, path
from home import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="home"),
]
