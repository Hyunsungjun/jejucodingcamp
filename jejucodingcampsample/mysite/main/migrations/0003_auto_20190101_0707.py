# Generated by Django 2.1 on 2019-01-01 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_cafe_mainphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='cafe',
            name='modifiedDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cafe',
            name='publishedDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]