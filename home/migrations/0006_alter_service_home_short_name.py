# Generated by Django 3.2.7 on 2021-09-18 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210916_0304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service_home',
            name='short_name',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
