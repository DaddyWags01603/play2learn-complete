from django.urls import path

from .views import ContactUsView, ContactThanksView

app_name = 'contact'
urlpatterns = [
    path('contact/', ContactUsView.as_view(), name='contact'),
    path('thanks/', ContactThanksView.as_view(), name='thanks'),
]