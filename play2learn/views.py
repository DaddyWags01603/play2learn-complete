from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages


class AboutUsView(TemplateView):
    template_name = "about_us.html"

    def get(self, request, *args, **kwargs):
        messages.debug(request, 'Debug message.')
        messages.info(request, 'Info message.')
        messages.success(request, 'Success message.')
        messages.warning(request, 'Warning message.')
        messages.error(request, 'Error message.')
        return super().get(request, args, kwargs)

class AdminView(TemplateView):
    template_name = "admin.html"

class ContactUsView(TemplateView):
    template_name = "contact-us.html"

class HomePageView(TemplateView):
    template_name = "home.html"

class LeaderboardsView(TemplateView):
    template_name = "leaderboards.html"

class ReviewUsView(TemplateView):
    template_name = "review-us.html"