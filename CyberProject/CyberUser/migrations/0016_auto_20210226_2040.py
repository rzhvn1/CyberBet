# Generated by Django 3.1.6 on 2021-02-26 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CyberUser', '0015_bet_money'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bet',
            old_name='match_result',
            new_name='match_res',
        ),
    ]
