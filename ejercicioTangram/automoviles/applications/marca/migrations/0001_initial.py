# Generated by Django 4.0.3 on 2022-03-21 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True, verbose_name='Marca')),
                ('fecha_fundacion', models.DateField(verbose_name='Fundacion')),
                ('telefono_atencion', models.IntegerField(unique=True, verbose_name='Telefono')),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
                'ordering': ['id'],
            },
        ),
    ]
