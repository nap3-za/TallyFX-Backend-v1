# Generated by Django 4.2.11 on 2025-01-24 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading_plan', '0004_tradingmodel_code_tradingmodel_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='default_journal',
            field=models.BooleanField(default=False),
        ),
    ]
