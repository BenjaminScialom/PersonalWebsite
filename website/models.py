# Create your models here.
from django.db import models
from django.utils import timezone


class Testimonial(models.Model):

    author = models.CharField(max_length=100)
    affiliation = models.CharField(max_length=100, blank=True)
    text = models.TextField()
    added = models.DateTimeField(default=timezone.now)
