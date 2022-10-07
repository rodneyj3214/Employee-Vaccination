# Generated by Django 3.2.16 on 2022-10-07 01:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20221005_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='Birthday'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message='Phone number must be in the format: +9999999. Up 15 digits allowed.', regex='\\+?1?\\d{9,15}$')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, validators=[django.core.validators.RegexValidator(message='Only letters and blank spaces are required', regex='^[a-zA-Z\\sÀ-ÿ\\u00f1\\u00d1\\s]*$')], verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, validators=[django.core.validators.RegexValidator(message='Only letters and blank spaces are required', regex='^[a-zA-Z\\sÀ-ÿ\\u00f1\\u00d1\\s]*$')], verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='vaccine',
            name='vaccine_date',
            field=models.DateField(verbose_name='Vaccine date'),
        ),
    ]
