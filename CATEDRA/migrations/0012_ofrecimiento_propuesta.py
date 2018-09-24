# Generated by Django 2.0.8 on 2018-09-10 18:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('CATEDRA', '0011_codigosde'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ofrecimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materia', models.CharField(max_length=200)),
                ('estrategia', models.CharField(max_length=200)),
                ('titulo', models.CharField(max_length=200)),
                ('horas', models.IntegerField(default=0)),
                ('codigode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CATEDRA.CodigosDE')),
            ],
        ),
        migrations.CreateModel(
            name='Propuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('escuela', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CATEDRA.Escuela')),
                ('ofrecimientos', models.ManyToManyField(blank=True, null=True, to='CATEDRA.Ofrecimiento')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CATEDRA.Empleado')),
            ],
        ),
    ]