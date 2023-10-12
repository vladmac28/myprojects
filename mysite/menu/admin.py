from django.contrib import admin

from .models import MenuItem, Menu


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    """
    Admin configuration for MenuItem model.
    """
    list_display = ('pk', 'title', 'parent')
    list_filter = ('menu',)
    search_fields = ('title', 'slug')
    ordering = ('pk',)

    fieldsets = (
        ('Add new item', {
            'description': "Parent should be a menu or item",
            'fields': (('menu', 'parent'), 'title', 'slug')
            }),
    )


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """
    Admin configuration for Menu model.
    """
    list_display = ('title', 'slug')
    search_fields = ('title', 'slug')
