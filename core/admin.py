from django.contrib import admin

from .models import User, Contact, City, Country


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'role', 'get_city', 'supplier')
    list_display_links = ('email', 'supplier',)
    ordering = ('email',)
    search_fields = ('email', )
    list_filter = ('contact__city__city_name', )
    actions = ['set_debts_to_zero']
    fieldsets = (
        ('Personal info', {'fields': ('name', 'email', 'contact', 'supplier', 'debts', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
    )

    @admin.action(description='Обнулить долги')
    def set_debts_to_zero(self, request, queryset):
        queryset.update(debts=0.00)

    @admin.display(ordering='contact__city__city_name', description='Город')
    def get_city(self, obj):
        if obj.contact:
            if city := obj.contact.city.city_name:
                return city
        return 'No city'


admin.site.register(User, CustomUserAdmin)
admin.site.register(Contact)
admin.site.register(City)
admin.site.register(Country)
