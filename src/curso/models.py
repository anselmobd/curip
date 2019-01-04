from django.db import models

class Trilha(models.Model):
    nome = models.CharField(
        max_length=100,
        verbose_name='Nome')

    def __str__(self):
        return self.nome

    class Meta:
        db_table = "c_trilha"
        verbose_name = "Trilha"
