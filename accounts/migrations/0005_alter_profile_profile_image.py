# Generated by Django 5.0.1 on 2024-02-27 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_profile_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='profile_default.png', null=True, upload_to='profile/'),
        ),
    ]
