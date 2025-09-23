from django.views.generic import TemplateView

# Create your views here.
class AdminView(TemplateView):
    template_name = "admin.html"

class AnagramHuntView(TemplateView):
    template_name = "anagram-hunt.html"

class ContactUsView(TemplateView):
    template_name = "contact-us.html"

class HomePageView(TemplateView):
    template_name = "home.html"

class LeaderboardsView(TemplateView):
    template_name = "leaderboards.html"

class LoginView(TemplateView):
    template_name = "login.html"

class MathFactsView(TemplateView):
    template_name = "math-facts.html"

class MyAccountView(TemplateView):
    template_name = "my-account.html"

class RegisterView(TemplateView):
    template_name = "register.html"

class ReviewUsView(TemplateView):
    template_name = "review-us.html"
