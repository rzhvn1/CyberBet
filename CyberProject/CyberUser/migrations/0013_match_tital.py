# Generated by Django 3.1.6 on 2021-02-26 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CyberUser', '0012_auto_20210224_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='tital',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]