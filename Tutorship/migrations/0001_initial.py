# Generated by Django 4.0.4 on 2022-06-06 19:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Student', '0001_initial'),
        ('UserAuthentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_people', models.IntegerField()),
                ('url', models.URLField(blank=True, null=True)),
                ('state', models.CharField(choices=[('AP', 'Aprobada'), ('DN', 'Realizada')], default='AP', max_length=2)),
                ('name', models.CharField(max_length=80, null=True)),
                ('description', models.CharField(max_length=500, null=True)),
                ('request', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Student.request')),
            ],
        ),
        migrations.CreateModel(
            name='TutorshipScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('student_comment', models.TextField(null=True)),
                ('tutorship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tutorship.tutorship')),
            ],
        ),
        migrations.CreateModel(
            name='RequestNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_type', models.CharField(choices=[('RE', 'Nueva solicitud'), ('AR', 'Solicitud aceptada'), ('RR', 'Solicitud rechazada')], max_length=2)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('seen', models.BooleanField(default=False)),
                ('from_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to='UserAuthentication.user')),
                ('request', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Student.request')),
                ('to_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to='UserAuthentication.user')),
            ],
        ),
    ]
