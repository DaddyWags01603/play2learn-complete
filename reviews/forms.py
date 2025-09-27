from django.forms import ModelForm, Textarea

from .models import review

class ReviewForm(ModelForm):
    class Meta:
        model = review
        fields = ['name', 'email', 'rating', 'comments']
        widgets = {
            'name': Textarea(attrs={'autofocus': True, 'rows': 1, 'cols': 40}),
            'email': Textarea(attrs={'rows': 1, 'cols': 40}),
            'comments': Textarea(attrs={'rows': 4, 'cols': 40}),
        }
        labels = {
            'name': 'Name',
            'email': 'Email',
            'rating': 'Rating (1-5)',
            'comments': 'Comments',
        }
        help_texts = {
            'name': 'Enter your name.',
            'email': 'Enter a valid email address.',
            'rating': 'Rate from 1 (worst) to 5 (best).',
            'comments': 'Provide any additional feedback here.',
        }