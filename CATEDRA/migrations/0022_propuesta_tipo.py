# Generated by Django 2.0.8 on 2018-10-12 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CATEDRA', '0021_servicio'),
    ]

    operations = [
        migrations.AddField(
            model_name='propuesta',
            name='tipo',
            field=models.CharField(choices=[('Maestros', 'Maestros'), ('Padres', 'Padres')], default='Maestros', max_length=200),
        ),
    ]
