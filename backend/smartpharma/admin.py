from django.contrib import admin
from .models import Meds, Accounts

# Register your models here.
class MedsAdmin(admin.ModelAdmin):
    list_display = ("prodName", "amtPerscribed", "amtInStock")
    
admin.site.register(Meds, MedsAdmin)

class AccountsAdmin(admin.ModelAdmin):
    list_display = ("username", "password")