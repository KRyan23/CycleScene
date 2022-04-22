# Generated by Django 3.2 on 2022-04-22 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, null=True)),
                ('titlerepair', models.CharField(max_length=254, null=True)),
                ('bodyrepair', models.TextField(blank=True, default=True)),
                ('titlerescue', models.CharField(max_length=254, null=True)),
                ('bodyrescue', models.TextField(blank=True, default=True)),
                ('service1', models.TextField(blank=True, default=True)),
                ('service2', models.TextField(blank=True, default=True)),
            ],
        ),
    ]
