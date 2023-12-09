from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'updated_at', 'status', 'get_photo',)
    list_display_links = ('name', 'get_photo')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

    def get_photo(self, obj):
        return mark_safe(f"<img src={obj.image.url} width='65' height='40/>'")

    get_photo.short_description = 'Image'


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'updated_at', 'status', 'get_photo',)
    list_display_links = ('name', 'get_photo',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

    def get_photo(self, obj):
        return mark_safe(f"<img src={obj.image.url} width='65' height='40/>'")

    get_photo.short_description = 'Image'


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'updated_at', 'status', 'get_photo', 'sub_category')
    list_display_links = ('name', 'get_photo',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('sub_category',)

    def get_photo(self, obj):
        return mark_safe(f"<img src={obj.image.url} width='65' height='40/>'")

    get_photo.short_description = 'Image'
