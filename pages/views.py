from django.views.generic import TemplateView
from reviews.models import review

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # add the reviews queryset to the template context
        context["reviews"] = review.objects.order_by("-created")[:10]
        return context

class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'