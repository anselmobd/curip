from django.db import models
from django.core.validators import MinValueValidator


class Trilha(models.Model):
    nome = models.CharField(
        max_length=100,
        verbose_name='Nome',
    )
    meses = models.DecimalField(
        'Duração (meses)',
        max_digits=3,
        decimal_places=1,
        default=0,
        validators=[MinValueValidator(0)]
    )
    idade = models.PositiveIntegerField(
        'Idade inicial',
        default=11,
    )
    material = models.DecimalField(
        'Material Didádico',
        max_digits=6,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0)]
    )

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
