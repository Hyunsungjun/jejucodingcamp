# Generated by Django 2.1 on 2019-01-01 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cafe',
            name='mainphoto',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
