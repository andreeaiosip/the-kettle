# Generated by Django 3.1.2 on 2020-10-17 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20201017_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tea',
            name='tea_bags',
            field=models.IntegerField(),
        ),
    ]
