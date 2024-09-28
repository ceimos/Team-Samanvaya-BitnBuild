from django.contrib import admin

# Register your models here.
from .models import Cloth, Outfit, OutfitCloth, Donation, Sell, SustainibilityDetails

admin.site.register(Cloth)
admin.site.register(Outfit)
admin.site.register(OutfitCloth)
admin.site.register(Donation)
admin.site.register(Sell)
admin.site.register(SustainibilityDetails)