from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from goods.models import Product, Supplier, Contact

class CustomSupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_city', 'link_to_provider')
    list_display_links = ('name', )
    ordering = ('created',)
    list_filter = ('contact__city', )
    actions = ['set_debts_to_zero']


    def link_to_provider(self, obj):
        if not obj.provider:
            return None

        url = reverse("admin:goods_supplier_change", args=[obj.provider.id])
        link = f'<a href="{url}">{obj.provider.name}</a>'

        return mark_safe(link)
    link_to_provider.short_description = 'Поставщик'


    @admin.action(description='Обнулить долги')
    def set_debts_to_zero(self, request, queryset):
        queryset.update(debts=0.00)

    @admin.display(ordering='contact__city__city_name', description='Город')
    def get_city(self, obj):
        if obj.contact:
            if city := obj.contact.city:
                return city
        return 'No city'

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Supplier, CustomSupplierAdmin)
