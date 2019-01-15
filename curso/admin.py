from django.contrib import admin

from .models import Trilha, Curso


@admin.register(Trilha)
class TrilhaAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    ordering = ['nome']
    list_display = ['__str__', 'meses', 'idade', 'material']
    list_editable = ('meses', 'idade', 'material')


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    search_fields = ['trilha__nome', 'nome']
    ordering = ['trilha__nome', 'ordem', 'nome']
    list_display = [
        '__str__', 'ordem', 'carga', 'material', 'mensalidade', 'meses']
    list_editable = ('ordem', 'carga', 'material', 'mensalidade', 'meses')
