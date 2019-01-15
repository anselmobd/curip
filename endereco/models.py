from django.db import models


class UF(models.Model):
    sigla = models.CharField(
        min_length=2,
        max_length=2,
    )
    nome = models.CharField(
        max_length=60,
    )

    def __str__(self):
        return '{}-{}'.format(self.sigla, self.nome)

    class Meta:
        db_table = "c_uf"
