# Generated by Django 4.0.4 on 2022-06-06 19:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UserAuthentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date_sent', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_user_receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='original_user_receiver', to='UserAuthentication.user')),
                ('original_user_sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='original_user_sender', to='UserAuthentication.user')),
            ],
        ),
        migrations.CreateModel(
            name='MessageNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_type', models.CharField(choices=[('NM', 'New Message'), ('NR', 'New Reply')], max_length=2)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('seen', models.BooleanField(default=False)),
                ('from_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_from', to='UserAuthentication.user')),
                ('message', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Chat.message')),
                ('to_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_to', to='UserAuthentication.user')),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Chat.room'),
        ),
        migrations.AddField(
            model_name='message',
            name='user_sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserAuthentication.user'),
        ),
    ]