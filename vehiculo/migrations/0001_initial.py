# Generated by Django 4.2.16 on 2024-11-03 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(choices=[('FIAT', 'Fiat'), ('CHEVROLET', 'Chevrolet'), ('FORD', 'Ford'), ('TOYOTA', 'Toyota')], default='FORD', max_length=20)),
                ('modelo', models.CharField(max_length=100)),
                ('serial_carroceria', models.CharField(max_length=50)),
                ('serial_motor', models.CharField(max_length=50)),
                ('categoria', models.CharField(choices=[('PARTICULAR', 'Particular'), ('TRANSPORTE', 'Transporte'), ('CARGA', 'Carga')], default='PARTICULAR', max_length=20)),
                ('precio', models.PositiveSmallIntegerField()),
                ('fecha_creacion', models.DateField()),
                ('fecha_modificacion', models.DateTimeField()),
            ],
        ),
    ]
