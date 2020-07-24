from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Categories(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class ListingPage(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=200)
    startbids = models.IntegerField()
    imageurl = models.URLField(max_length=200)
    category = models.ForeignKey(Categories, blank=True, null=True, on_delete=models.CASCADE, related_name='listingtype')

    def __str__(self):
        return f"{self.title} at {self.startbids} usd"
    