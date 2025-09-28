from django.contrib import admin
from .models import Score

# Register your models here.
@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "game_type", "score", "duration", "created")
    list_filter = ("game_type", "created")
    readonly_fields = ("created",)
