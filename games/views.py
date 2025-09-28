import json
from django.http import JsonResponse
from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.
class MathFactsView(TemplateView):
    template_name = "math-facts.html"

class AnagramHuntView(TemplateView):
    template_name = "anagram-hunt.html"

def submit_score(request):
    if request.method == "POST":
        # process the submitted score data
        # (you would typically validate and save this data)
        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)