from django.urls import path

from .views import (
    ReviewCreateView, ReviewDeleteView, ReviewDetailView, ReviewListView, ReviewUpdateView
)

app_name = 'reviews'
urlpatterns = [
    path('review/create/', ReviewCreateView.as_view(), name='create'),
    path('review/<slug>/delete/', ReviewDeleteView.as_view(), name='delete'),
    path('review/<slug>/', ReviewDetailView.as_view(), name='detail'),
    path('review/<slug>/update', ReviewUpdateView.as_view(), name='update'),
    path('', ReviewListView.as_view(), name='list'),
]
