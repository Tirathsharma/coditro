# Generated by Django 3.2.7 on 2021-09-15 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_about_image_1_about_page_background_banner_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about_page',
            name='about_image_2',
            field=models.ImageField(blank=True, null=True, upload_to='about/'),
        ),
        migrations.AlterField(
            model_name='about_page',
            name='about_image_3',
            field=models.ImageField(blank=True, null=True, upload_to='about/'),
        ),
        migrations.AlterField(
            model_name='about_page',
            name='about_image_4',
            field=models.ImageField(blank=True, null=True, upload_to='about/'),
        ),
    ]
