# Generated by Django 2.0.8 on 2018-09-10 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CATEDRA', '0009_auto_20180907_1026'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='visita',
            options={'get_latest_by': 'fecha'},
        ),
        migrations.AlterField(
            model_name='empleado',
            name='municipio',
            field=models.ManyToManyField(blank=True, null=True, to='CATEDRA.Municipio'),
        ),
    ]