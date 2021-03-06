# Generated by Django 2.1.5 on 2019-01-15 19:37

from django.db import migrations


def load_endereco_uf_fixture(apps, schema_editor):
    from django.core.management import call_command
    call_command("loaddata", "0002_endereco_uf_fixture")


def delete_endereco_uf_all(apps, schema_editor):
    TipoImagem = apps.get_model("endereco", "Uf")
    TipoImagem.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            load_endereco_uf_fixture, delete_endereco_uf_all),
    ]
