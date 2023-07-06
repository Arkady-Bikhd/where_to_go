from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin, SortableTabularInline


class ImagePreviewMixin:
    def preview(self, image):
        image_url = image.image_url
        height = 200
        return format_html(
            '<img src="{}" height={} />',
            image_url, height
        )


class ImageInline(SortableTabularInline, admin.TabularInline, ImagePreviewMixin):
    model = Image
    fields = ('image', 'preview', 'image_number')
    ordering = ['image_number']
    readonly_fields = ['preview']   
   # preview = ImagePreviewMixin.preview
  #  preview.short_description = 'Просмотр'
    extra = 3


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):    
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin, ImagePreviewMixin):
    preview = ImagePreviewMixin.preview
    readonly_fields = ['preview']
