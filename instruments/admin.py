from django.contrib import admin
from instruments.models import Instrument, Brand

class InstrumentAdmin(admin.ModelAdmin):
    list_display = ('product','category','model', 'brand', 'price', 'condition')
    search_fields = ('product','model', 'brand', 'category')


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Instrument, InstrumentAdmin)
admin.site.register(Brand, BrandAdmin)
