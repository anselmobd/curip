from django.contrib import admin

from .models import Trilha


@admin.register(Trilha)
class TrilhaAdmin(admin.ModelAdmin):
    pass
