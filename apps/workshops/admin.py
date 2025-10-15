from django.contrib import admin
from .models import WorkshopStatus,Workshop,WorkshopGallery
# Register your models here.

@admin.register(WorkshopStatus)
class WorkshopStatusAdmin(admin.ModelAdmin):
    list_display = ('status_name',)

@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('status','title','place','teacher','is_active','datetime_holding')

@admin.register(WorkshopGallery)
class WorkshopGalleryAdmin(admin.ModelAdmin):
    list_display = ('workshop','image')