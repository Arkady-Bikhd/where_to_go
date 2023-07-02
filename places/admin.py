from django.contrib import admin
from .models import Place, PlaceImage
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin


def preview_image(self, place_image):
    return format_html(
        '<img src="{url}" height=200 />',
        url=place_image.image.url
        )


class PlaceImageInline(SortableInlineAdminMixin, admin.TabularInline):    
    model = PlaceImage
    fields = ('image', 'preview_image', 'image_number')
    ordering = ['image_number']
    preview_image = preview_image
    readonly_fields = ('preview_image',)   
    preview_image.short_description = 'Просмотр'
    extra = 3


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):    
    inlines = [
        PlaceImageInline,
    ]


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    preview_image = preview_image
    readonly_fields = ('preview_image',)
    