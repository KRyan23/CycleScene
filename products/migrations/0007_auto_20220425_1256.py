# Generated by Django 3.2 on 2022-04-25 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20220323_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='instock',
            field=models.BooleanField(default=True),
        ),
    ]