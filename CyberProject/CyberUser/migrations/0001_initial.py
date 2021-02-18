# Generated by Django 3.1.6 on 2021-02-18 12:20

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='default-profile-image', upload_to='')),
                ('full_name', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.PositiveIntegerField(null=True)),
                ('address', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('F', 'F'), ('M', 'M')], max_length=20)),
                ('description', models.CharField(max_length=50)),
                ('birth_day', models.DateField(default=datetime.date(2021, 2, 18))),
                ('wallet', models.PositiveIntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]