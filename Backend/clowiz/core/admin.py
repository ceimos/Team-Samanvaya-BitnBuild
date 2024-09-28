from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import Cloth, Outfit, OutfitCloth, Donation, Sell, SustainibilityDetails, User

admin.site.register(Cloth)
admin.site.register(User)
admin.site.register(Outfit)
admin.site.register(OutfitCloth)
admin.site.register(Donation)
admin.site.register(Sell)
admin.site.register(SustainibilityDetails)


#admin.site.register(User, UserAdmin)