from django.views.generic import TemplateView
from django.shortcuts import render
from django.conf import settings
from assessment.learnosity import generated_request_Items

# class ItemsAPIAssessmentView(TemplateView):
#     template_name = "items-api-assessment.html"

#     def get(self, request):
#         return render(request, self.template_name, {"title": "Items API Assessment"})
    

def itemsAPIAssessment(request):
    context = dict()
    context['generated_request'] = generated_request_Items
    context['title'] = "Items API Assessment"
    return render(request, 'items-api-assessment.html', context )