from django.views.generic import ListView

from reviews.models import review

class ReviewPanel(ListView):
    model = review

    def last_10_reviews(self):
        return review.objects.all().order_by('-created')[:10]
    
