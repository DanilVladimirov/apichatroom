from django.db import models
from django.utils import timezone
from django.core.validators import MaxLengthValidator, MinLengthValidator


class Message(models.Model):
    author = models.EmailField()
    text = models.TextField(default='', validators=[MinLengthValidator(1), MaxLengthValidator(100)])
    create_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.text[:10]}...'
