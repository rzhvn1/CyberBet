# Generated by Django 3.1.6 on 2021-02-24 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CyberUser', '0008_auto_20210220_1837'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('win_count', models.PositiveIntegerField(default=0)),
                ('lose_count', models.PositiveIntegerField(default=0)),
                ('tie_count', models.PositiveIntegerField(default=0)),
                ('rank', models.PositiveIntegerField(default=25)),
                ('moral', models.PositiveIntegerField(default=50)),
            ],
        ),
        migrations.CreateModel(
            name='TeamA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CyberUser.team')),
            ],
        ),
        migrations.CreateModel(
            name='TeamB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CyberUser.team')),
            ],
        ),
        migrations.CreateModel(
            name='Wager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_result', models.CharField(choices=[('W', 'W'), ('T', 'T'), ('L', 'L')], max_length=10)),
                ('teamA', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CyberUser.teama')),
                ('teamB', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CyberUser.teamb')),
            ],
        ),
    ]
