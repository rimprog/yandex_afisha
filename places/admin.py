from django.contrib import admin
from django.utils.html import format_html

from places.models import Place, Image

from adminsortable2.admin import SortableInlineAdminMixin


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ['get_preview']
    fields = ['image', 'get_preview', 'index_number']
    extra = 0

    def get_preview(self, instance):
        image_preview_html = format_html(
            '<img src="{url}" width="{width}" height={height} style="max-width:{max_width};max-height:{max_height};" />',
            url = instance.image.url,
            width=instance.image.width,
            height=instance.image.height,
            max_width = '300px',
            max_height = '200px',
        )

        return image_preview_html


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    search_fields = ['title']


admin.site.register(Image)
