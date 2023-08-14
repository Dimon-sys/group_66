from django.contrib import admin
from .models import Advertisement
from django.utils.html import format_html



class AdvertisementAdmin(admin.ModelAdmin):
    list_display =['id', 'title', 'description', 'price', 'auction', 'created_date', 'updated_date', 'image', 'get_thumbnail']
    list_filter = ['auction', 'created_at']

    actions = ['make_auction_as_false', 'make_auction_as_true']


    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction = False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction = True)

    @admin.display(description='Изображение')
    def get_thumbnail(self, obj):
        if obj.image:
            thumbnail_url = obj.image.url
            return format_html(f'<img src="{thumbnail_url}" width="100">')
        else:
            return format_html(f'<img src="/static/img/adv.png" width="100">')




    fieldsets = (
        ('Общее', {
            'fields' : ('title', 'description', 'image'),
        }),
        ('Финансы', {
            'fields' : ('price', 'auction'),
            'classes' : ['collapse'],
        })
    )

admin.site.register(Advertisement, AdvertisementAdmin)
# Register your models here.