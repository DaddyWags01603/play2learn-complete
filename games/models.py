from django.conf import settings
from django.db import models

# Create your models here.
class Score(models.Model):
    GAME_TYPES = [
        ('math-facts', "Math Facts"),
        ("anagram-hunt", "Anagram Hunt"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="scores"
    )
    game_type = models.CharField(max_length=50, choices=GAME_TYPES)
    duration = models.DurationField(help_text="Time taken to complete the game")
    score = models.IntegerField()
    settings = models.JSONField(default=dict, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.user} - {self.game_type} - {self.score}"