# Generated by Django 5.0.6 on 2024-06-10 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_settings_delete_usersettings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadexchangerate',
            name='rate',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='eurexchangerate',
            name='rate',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='settings',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='settings',
            name='selected_currencies',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='settings',
            name='start_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='usdexchangerate',
            name='rate',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
    ]
