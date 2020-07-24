from django.contrib import admin

from .models import Categories, ListingPage

# Register your models here.
admin.site.register(Categories)
admin.site.register(ListingPage)