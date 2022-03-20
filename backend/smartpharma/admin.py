from django.contrib import admin
from .models import Meds

# Register your models here.
class MedsAdmin(admin.ModelAdmin):
    list_display = ("prodName", "amtPerscribed", "amtInStock")
    
admin.site.register(Meds, MedsAdmin)