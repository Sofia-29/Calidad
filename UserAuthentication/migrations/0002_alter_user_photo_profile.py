# Generated by Django 3.2.5 on 2022-07-04 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserAuthentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo_profile',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
