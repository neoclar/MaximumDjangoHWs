from django.contrib import admin
from .models import Advertisement
# Register your models here.

# Управление объявлениями админкой:

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_at', 'auction', 'image', 'user']
    list_filter = ['auction', 'created_at']
    actions = ['auction_to_false', 'auction_to_true']
    fieldsets = (
        ('Общее', {
            'fields': ('title', 'description', 'image', 'user')
            }
        ),
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
            }
        )
    )

    @admin.action(description='Убрать возможность торга')
    def auction_to_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='Добавить возможность торга')
    def auction_to_true(self, request, queryset):
        queryset.update(auction=True)

admin.site.register(Advertisement, AdvertisementAdmin)