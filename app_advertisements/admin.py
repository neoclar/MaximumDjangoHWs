from django.contrib import admin
from .models import Advertisement
from django.utils.html import format_html
# from django.utils.formats import date_format
# Register your models here.

# Управление объявлениями админкой:
# from django.conf.locale.es import formats as es_formats
# es_formats.DATETIME_FORMAT = "d M Y H:i:s"
class AdvertisementAdmin(admin.ModelAdmin):
    # def created_at(self, obj):
    #     return obj.timefield.strftime("%d %b %Y %H:%M:%S")
    # created_at.admin_order_field = 'timefield'
    # created_at.short_description = 'Precise Time'
    # date_hierarchy = 'pub_date'
    list_display = ['id', 'title', 'description', 'price', 'created_at_view', 'update_at_view', 'auction', 'image_view', 'user']
    list_filter = ['auction', 'created_at', 'update_at']
    search_fields = ['title']
    # date_hierarchy = 
    list_display_links = ['id', 'title']
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

    # def get_list_display(self, request):
    #     # Получаем формат даты из настроек Django
    #     date_format_string = date_format('%d%m%Y')
        
    #     # Возвращаем список атрибутов модели и формат даты
    #     return ['attribute_name', 'another_attribute_name', 'date_field_name', date_format_string]


admin.site.register(Advertisement, AdvertisementAdmin)