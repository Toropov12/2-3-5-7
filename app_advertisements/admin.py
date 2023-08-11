from django.contrib import admin
from .models import Advertisements
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_date', 'auction', 'image']
    list_filter = ['auction', 'created_at']
    actions = ['make_auction_as_false', 'make_auction_as_true']
admin.site.register(Advertisements, AdvertisementAdmin)


# Register your models here.
