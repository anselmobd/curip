from django.db import models

class Trilha(models.Model):
    nome = models.CharField(
        max_length=100,
        verbose_name='Nome')

    def __str__(self):
        return self.nome

    class Meta:
        db_table = "c_trilha"

class Curso(models.Model):
    trilha = models.ForeignKey(
        Trilha, on_delete=models.CASCADE)
    nome = models.CharField(
        max_length=100,
        verbose_name='Nome')

    def __str__(self):
        return '({}) {}'.format(self.trilha.nome, self.nome)

    class Meta:
        db_table = "c_curso"
