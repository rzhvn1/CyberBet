# Generated by Django 3.1.6 on 2021-02-19 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CyberUser', '0004_auto_20210219_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='comments',
        ),
    ]
