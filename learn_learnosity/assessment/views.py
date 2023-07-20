from django.views.generic import TemplateView
from django.shortcuts import render
from learnosity_sdk.request import Init


class ItemsAPIAssessmentView(TemplateView):
    template_name = "items-api-assessment.html"

    def get(self, request):
        return render(request, self.template_name, {"title": "Items API Assessment"})