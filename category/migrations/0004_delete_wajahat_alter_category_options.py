# Generated by Django 5.0.1 on 2024-01-29 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_wajahat'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Wajahat',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Categories', 'verbose_name_plural': 'Categories'},
        ),
    ]