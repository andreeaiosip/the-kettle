# Generated by Django 3.1.2 on 2020-11-08 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('body', models.TextField()),
                ('image', models.ImageField(default='static/img/no-img.jpg', upload_to='static/img')),
            ],
        ),
    ]
