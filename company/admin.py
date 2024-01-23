from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from company.models import Company, Contacts, Product


@admin.register(Company)
class AdminCompany(admin.ModelAdmin):
    list_display = ('title', 'subjects_electronic_network', 'provider_link',
                    'debt', 'date_created', 'contacts_city',)
    list_filter = ('contacts__city',)
    actions = ['debt_removal']

    def provider_link(self, obj):
        if obj.provider:
            url = reverse("admin:company_company_change", args=[obj.provider.pk])
            return format_html('<a href="{}">{}</a>', url, obj.provider.title)
        return '-'
    provider_link.short_description = 'Поставщик'

    def contacts_city(self, obj):
        if obj.contacts.city:
            return obj.contacts.city
        return '-'
    contacts_city.short_description = 'Город'

    @admin.action(description='Удалить задолженность перед поставщиком')
    def debt_removal(self, request, queryset):
        queryset.update(debt=0)


@admin.register(Contacts)
class AdminContacts(admin.ModelAdmin):
    list_display = ('email', 'country',)


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'company',)
