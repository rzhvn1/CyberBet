# Generated by Django 3.1.6 on 2021-03-03 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CyberUser', '0022_auto_20210303_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bet',
            name='money',
            field=models.FloatField(default=0),
        ),
    ]
