from django.urls import include, path
from . import views

urlpatterns = [
    path("items-api", views.itemsAPIAssessment, name="items-api-assessment"),
]
