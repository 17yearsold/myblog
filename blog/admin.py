from django.contrib import admin

from . import models
from .models import Article, Category, Tag
from django.utils import timezone


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_time', 'modified_time', 'author', 'categories']
    fieldsets = [('基础信息', {'fields': ['title', 'author', 'tags']}),
                 ('详细信息', {'fields': ['summary', 'body']})]

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)
