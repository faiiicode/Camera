# Generated by Django 3.2.15 on 2022-10-31 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cameraapp', '0007_auto_20221031_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callback',
            name='name',
            field=models.CharField(max_length=257, unique=True),
        ),
    ]