# Generated by Django 5.0 on 2024-01-02 00:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0001_initial'),
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bet',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bet_on_match', to='schedule.schedule'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.schedule'),
        ),
    ]
