# Generated by Django 3.2.6 on 2021-08-29 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0010_auto_20210829_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentbase',
            name='view_counter',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
