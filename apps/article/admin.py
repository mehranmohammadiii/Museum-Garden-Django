from django.contrib import admin
from .models import Author,ArticleType,Article,ArticleGallery
# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name","family","email","mobile","is_active")

@admin.register(ArticleType)
class ArticleTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("articletype","subject","register_date","publication_date","update_date","is_active","view_number")

@admin.register(ArticleGallery)
class ArticleGalleryAdmin(admin.ModelAdmin):
    list_display = ("name","article")

