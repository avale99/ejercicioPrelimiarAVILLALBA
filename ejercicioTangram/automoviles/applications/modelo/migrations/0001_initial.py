# Generated by Django 4.0.3 on 2022-03-21 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True, verbose_name='Modelo')),
                ('carroceria', models.CharField(choices=[('0', 'Sedán'), ('1', 'Familiar'), ('2', 'Coupé'), ('3', 'Todoterreno'), ('4', 'Descapotable'), ('5', 'SUV')], max_length=1, verbose_name='Carroceria')),
            ],
            options={
                'verbose_name': 'Modelo',
                'verbose_name_plural': 'Modelos',
                'ordering': ['id'],
            },
        ),
    ]
