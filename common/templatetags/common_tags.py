import random
from django import template

from reviews.models import review

register = template.Library()

@register.inclusion_tag('common/joke.html')
def random_joke():
    count = review.objects.count()
    if count > 0: # In case we haven't added any jokes yet
        i = random.randint(0, count-1)
        joke = review.objects.all()[i]
        return {'review': review}
    else:
        return {
            'review': {
                'name': 'Me?',
                'email': 'Temail@server.com',
                'rating': 5,
                'comments': 'Nothing could be better!',
            }
        }