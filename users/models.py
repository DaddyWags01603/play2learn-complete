from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions

# Create your models here.
def validate_avatar(value):
    w, h = get_image_dimensions(value)
    if w > 200 or h > 200:
        raise ValidationError("Avatar dimensions should not exceed 200x200 pixels.")

class CustomUser(AbstractUser):
    dob = models.DateField(
        verbose_name="Date of Birth", null=True, blank=True
    )
    avatar = models.ImageField(
        upload_to='avatars/', blank=True,
        help_text="Avatar image should not exceed 200x200 pixels.",
        validators=[validate_avatar]
    )
    
    def get_absolute_url(self):
        return reverse('my_account')
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.username})'