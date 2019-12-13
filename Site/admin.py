from django.contrib import admin
from Site.models import Chair, ChairImages


class ChairImageInline(admin.StackedInline):
    model = ChairImages
    extra = 0
    fields = ['photo_tag', 'image']
    readonly_fields = ['photo_tag', ]


class ChairAdmin(admin.ModelAdmin):
    readonly_fields = ['date']
    inlines = [ChairImageInline, ]

    list_display = ['name', 'id']


admin.site.register(Chair, ChairAdmin)

# Register your models here.
