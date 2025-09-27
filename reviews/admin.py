from django.contrib import admin
from .models import review

# Register your models here.
@admin.register(review)
class ReviewAdmin(admin.ModelAdmin):
    model = review
    list_display = ('name', 'email', 'comments', 'rating', 'created', 'updated')

    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing an existing object
            return ('slug', 'created', 'updated')
        return ()