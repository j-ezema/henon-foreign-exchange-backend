# Generated by Django 5.0.6 on 2024-06-08 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_exchangerate_base_currency'),
    ]

    operations = [
        migrations.CreateModel(
            name='CADExchangeRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=3)),
                ('date', models.DateField()),
                ('rate', models.DecimalField(decimal_places=6, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='EURExchangeRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=3)),
                ('date', models.DateField()),
                ('rate', models.DecimalField(decimal_places=6, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='USDExchangeRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=3)),
                ('date', models.DateField()),
                ('rate', models.DecimalField(decimal_places=6, max_digits=10)),
            ],
        ),
        migrations.DeleteModel(
            name='ExchangeRate',
        ),
    ]
