from django.contrib import admin

from .models import Trilha, Curso


@admin.register(Trilha)
class TrilhaAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    ordering = ['nome']
    pass


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    search_fields = ['trilha__nome', 'nome']
    ordering = ['trilha__nome', 'nome']
    pass
