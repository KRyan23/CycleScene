# Generated by Django 3.2 on 2022-03-23 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20220305_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='ean',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='feature1',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='feature2',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='feature3',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='feature4',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='instock',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True),
        ),
    ]