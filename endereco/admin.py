from django.contrib import admin

from .models import UF


@admin.register(UF)
class UfAdmin(admin.ModelAdmin):
    search_fields = ['__str__']
    ordering = ['__str__']
    list_display = ['__str__']
