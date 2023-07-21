from django.views.generic import TemplateView
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.conf import settings
from assessment.learnosity import generated_request_Items

# class ItemsAPIAssessmentView(TemplateView):
#     template_name = "items-api-assessment.html"

#     def get(self, request):
#         return render(request, self.template_name, {"title": "Items API Assessment"})
    

def itemsAPIAssessment(request):
    context = dict()
    context['title'] = "Items API Assessment"
    context['name'] = "Learn about Learnosity Example"
    context['generated_request'] = generated_request_Items
    return render(request, 'assessmentBase.html', context)