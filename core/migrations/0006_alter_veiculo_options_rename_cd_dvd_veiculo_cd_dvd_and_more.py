# Generated by Django 4.2.2 on 2023-07-28 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_veiculo_ar_condicionado_veiculo_cd_dvd'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='veiculo',
            options={'verbose_name': 'Veiculos', 'verbose_name_plural': 'Veiculos'},
        ),
        migrations.RenameField(
            model_name='veiculo',
            old_name='cd_dvd',
            new_name='CD_DVD',
        ),
        migrations.AlterUniqueTogether(
            name='veiculo',
            unique_together={('renavam', 'placa')},
        ),
        migrations.AlterModelTable(
            name='veiculo',
            table='Veiculo',
        ),
    ]