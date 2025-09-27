from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView
from reviews.models import review

# Create your views here.
from .forms import ReviewForm
from .models import review

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = review
    form_class = ReviewForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = review
    success_url = reverse_lazy('reviews:list')

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user

class ReviewDetailView(DetailView):
    model = review
    
class ReviewListView(ListView):
    model = review

class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = review
    form_class = ReviewForm

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user

class ReviewUsView(TemplateView):
    template_name = "review-us.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = review.objects.all()
        return context