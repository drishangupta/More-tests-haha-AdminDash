from django.contrib import admin
from .models import Datas
# Register your models here.
class DatasAdmin(admin.ModelAdmin):
    list_display=['ID',"name","email"]

admin.site.register(Datas,DatasAdmin)