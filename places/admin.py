from django.contrib import admin
from places.models import Place, PlaceDetails, Image


class ImageInline(admin.TabularInline):
    model = Image

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


admin.site.register(PlaceDetails)
admin.site.register(Image)
