# Generated by Django 2.0.8 on 2018-09-05 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CATEDRA', '0006_empleado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes/avatars/'),
        ),
    ]
