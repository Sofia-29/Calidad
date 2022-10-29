# Generated by Django 4.0.4 on 2022-06-09 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0001_initial'),
        ('Region', '0001_initial'),
        ('Modality', '0001_initial'),
        ('Session', '0001_initial'),
        ('Tutor', '0002_alter_tutor_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='modality_type',
            field=models.ManyToManyField(blank=True, null=True, to='Modality.modality'),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='payment_type',
            field=models.ManyToManyField(blank=True, null=True, to='Payment.payment'),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Region.regions'),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='session_type',
            field=models.ManyToManyField(blank=True, null=True, to='Session.session'),
        ),
    ]