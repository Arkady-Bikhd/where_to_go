from django.contrib import admin
from .models import Place, PlaceImage
from django.utils.html import format_html

def show_preview_image(self, place_image):

    return format_html('<img src="{url}" height=200 />',
                url= place_image.image.url)


class PlaceImageInline(admin.TabularInline):    
    model = PlaceImage
    fields = ('image', 'show_preview_image', 'image_number')
    show_preview_image = show_preview_image
    readonly_fields = ('show_preview_image',)   


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):    
    inlines = [
        PlaceImageInline,
    ]


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    show_preview_image = show_preview_image
    readonly_fields = ('show_preview_image',)



