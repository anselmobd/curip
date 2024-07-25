import re

from django.db import models
from django.core.validators import MinLengthValidator


class Uf(models.Model):
    sigla = models.CharField(
        max_length=2,
        validators=[MinLengthValidator(2)]
    )
    nome = models.CharField(
        max_length=60,
    )

    def __str__(self):
        return '{}-{}'.format(self.sigla, self.nome)

    class Meta:
        db_table = "c_uf"
        verbose_name = "UF"
        verbose_name_plural = "UFs"

    def save(self, *args, **kwargs):
        self.sigla = self.sigla and self.sigla.upper()
        super().save(*args, **kwargs)


class Endereco(models.Model):
    cep = models.PositiveIntegerField(
        'CEP',
        default=0,
    )
    logradouro = models.CharField(
        max_length=120,
    )
    numero = models.PositiveIntegerField(
        'Número',
        default=0,
    )
    complemento = models.CharField(
        max_length=60,
        null=True, blank=True,
    )
    bairro = models.CharField(
        max_length=60,
        null=True, blank=True,
    )
    cidade = models.CharField(
        max_length=60,
    )
    uf = models.ForeignKey(
        Uf, on_delete=models.PROTECT,
        verbose_name='UF',
    )

    def __str__(self):
        cep = '{}-{}'.format(*(re.findall(r'\d{5}|\d{3}', str(self.cep))))
        result = '{}; {:n}'.format(cep, self.numero)
        if self.complemento is not None:
            result = '; '.join([result, self.complemento])
        return result

    class Meta:
        db_table = "c_endereco"
        verbose_name = "Endereço"
