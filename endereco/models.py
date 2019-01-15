from django.db import models
from django.core.validators import MinLengthValidator


class UF(models.Model):
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
        super(UF, self).save(*args, **kwargs)
