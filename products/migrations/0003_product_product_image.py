# Generated by Django 5.0.1 on 2024-02-09 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_created_at_product_slug_product_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='', upload_to='product/'),
            preserve_default=False,
        ),
    ]