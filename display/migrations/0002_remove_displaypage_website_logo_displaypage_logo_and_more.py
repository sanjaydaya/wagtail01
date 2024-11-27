# Generated by Django 5.1.3 on 2024-11-27 07:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0001_initial'),
        ('wagtailimages', '0027_image_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='displaypage',
            name='website_logo',
        ),
        migrations.AddField(
            model_name='displaypage',
            name='logo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AlterField(
            model_name='displaypage',
            name='banner_button_text',
            field=models.CharField(default='Click', max_length=50),
        ),
        migrations.AlterField(
            model_name='displaypage',
            name='banner_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AlterField(
            model_name='displaypagesponsor',
            name='sponsor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='display.sponsor'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sponsors_images', to='wagtailimages.image'),
        ),
    ]