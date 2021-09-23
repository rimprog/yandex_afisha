from django.contrib import admin
from places.models import Place, PlaceDetails, Image
from django.utils.html import format_html


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ['get_preview']
    fields = ['image', 'get_preview', 'index_number']

    def get_preview(self, instance):
        image_preview_html = format_html(
            '<img src="{url}" width="{width}" height={height} />',
            url = instance.image.url,
            width=instance.image.width / 7,
            height=instance.image.height / 7,
        )

        return image_preview_html


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


admin.site.register(PlaceDetails)
admin.site.register(Image)
