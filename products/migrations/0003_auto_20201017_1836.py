# Generated by Django 3.1.2 on 2020-10-17 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20201017_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tea',
            name='tea_bags',
            field=models.DecimalField(decimal_places=2, max_digits=2),
        ),
    ]