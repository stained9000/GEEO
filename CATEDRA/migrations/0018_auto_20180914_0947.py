# Generated by Django 2.0.8 on 2018-09-14 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CATEDRA', '0017_ofrecimiento_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ofrecimiento',
            name='estado',
            field=models.CharField(choices=[('EN EVALUACION', 'EN EVALUACION'), ('APROBADA', 'APROBADA'), ('RECHAZADA', 'RECHAZADA')], default='EN EVALUACION', max_length=200),
        ),
    ]
