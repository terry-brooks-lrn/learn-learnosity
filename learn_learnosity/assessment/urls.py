from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.ItemsAPIAssessmentView.as_view(), name="items-api-assessment"),
]
