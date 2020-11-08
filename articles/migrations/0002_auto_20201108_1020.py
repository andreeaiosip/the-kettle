# Generated by Django 3.1.2 on 2020-11-08 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default='static/img/no-img.jpg', upload_to='static/img'),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]