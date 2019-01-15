import os

from django.contrib import admin

from curip import settings
from .models import Uf


@admin.register(Uf)
class UfAdmin(admin.ModelAdmin):
    search_fields = ['sigla', 'nome']
    ordering = ['sigla']
    list_display = ['__str__']

    class Media:
        static_url = getattr(settings, 'STATIC_URL', 'static')
        js = [os.path.join(static_url, 'admin', 'endereco', 'uf.js'), ]
