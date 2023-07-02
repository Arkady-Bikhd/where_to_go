from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin


def preview_image(self, place_image):
    return format_html(
        '<img src="{url}" height=200 />',
        url=place_image.image.url
        )


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    fields = ('image', 'preview_image', 'image_number')
    ordering = ['image_number']
    preview_image = preview_image
    readonly_fields = ('preview_image',)   
    preview_image.short_description = 'Просмотр'
    extra = 3


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):    
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    preview_image = preview_image
    readonly_fields = ('preview_image',)
