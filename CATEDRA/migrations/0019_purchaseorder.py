# Generated by Django 2.0.8 on 2018-09-24 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CATEDRA', '0018_auto_20180914_0947'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=200)),
                ('documento', models.FileField(upload_to='registros/po/')),
                ('ofrecimiento', models.ManyToManyField(to='CATEDRA.Ofrecimiento')),
                ('propuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CATEDRA.Propuesta')),
            ],
        ),
    ]
