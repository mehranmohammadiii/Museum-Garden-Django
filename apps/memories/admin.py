from django.contrib import admin
from .models import Memory,MemoryGallery

@admin.register(Memory)
class MemoryAdmin(admin.ModelAdmin):
    list_display = ('title','register_date','is_active','user_register')

@admin.register(MemoryGallery)
class MemoryGalleryAdmin(admin.ModelAdmin):
    list_display = ('image_name','memory')