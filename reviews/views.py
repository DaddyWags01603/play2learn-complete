from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
from .models import review
from .forms import ReviewForm

class ReviewCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = review
    form_class = ReviewForm
    success_message = "Review created"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = review
    success_url = reverse_lazy('reviews:list')

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        return result

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user
    
    def form_valid(self, form):
        messages.success(self.request, "Review deleted")
        return super().form_valid(form)

class ReviewDetailView(DetailView):
    model = review
    
class ReviewListView(ListView):
    model = review

class ReviewUpdateView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = review
    form_class = ReviewForm
    success_message = "Review updated"

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user

class ReviewUsView(TemplateView):
    template_name = "review-us.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = review.objects.all()
        return context