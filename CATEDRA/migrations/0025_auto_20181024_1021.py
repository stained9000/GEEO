# Generated by Django 2.0.8 on 2018-10-24 14:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('CATEDRA', '0024_auto_20181015_1142'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('numero', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('monto', models.IntegerField(default=0)),
                ('po', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CATEDRA.PurchaseOrder')),
            ],
        ),
        migrations.AlterField(
            model_name='codigosde',
            name='tipo',
            field=models.CharField(blank=True, choices=[('Colegio - Maestros', 'Colegio - Maestros'), ('Colegio - Padres', 'Colegio - Padres'), ('Publica - Maestros', 'Publica - Maestros'), ('Publica - Padres', 'Publica - Padres')], default='Publica - Maestros', max_length=200, null=True),
        ),
    ]