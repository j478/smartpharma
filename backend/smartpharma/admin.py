from django.contrib import admin
from .models import Smartpharma
# Register your models here.
class SmartpharmaAdmin(admin.ModelAdmin):
    list_display = ("prodName", "prodNum", "prodColor")
admin.site.register(Smartpharma, SmartpharmaAdmin)