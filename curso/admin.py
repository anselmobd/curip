from django.contrib import admin

from .models import Trilha, Curso


@admin.register(Trilha)
class TrilhaAdmin(admin.ModelAdmin):
    pass

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    pass
