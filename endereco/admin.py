from django.contrib import admin

from .models import UF


@admin.register(UF)
class UfAdmin(admin.ModelAdmin):
    search_fields = ['sigla', 'nome']
    ordering = ['sigla']
    list_display = ['__str__']
