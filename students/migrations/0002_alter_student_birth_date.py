# Generated by Django 5.1.6 on 2025-02-25 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birth_date',
            field=models.DateField(verbose_name='Дата рождения'),
        ),
    ]
