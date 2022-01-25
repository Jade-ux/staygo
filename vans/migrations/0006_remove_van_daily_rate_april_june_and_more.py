# Generated by Django 4.0.1 on 2022-01-25 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vans', '0005_alter_van_price_per_extra_mile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='van',
            name='daily_rate_april_june',
        ),
        migrations.RemoveField(
            model_name='van',
            name='daily_rate_december_march',
        ),
        migrations.RemoveField(
            model_name='van',
            name='daily_rate_july_september',
        ),
        migrations.RemoveField(
            model_name='van',
            name='daily_rate_october_november',
        ),
        migrations.AddField(
            model_name='van',
            name='daily_rate_april_to_june',
            field=models.DecimalField(decimal_places=2, default=110, max_digits=6),
        ),
        migrations.AddField(
            model_name='van',
            name='daily_rate_december_to_march',
            field=models.DecimalField(decimal_places=2, default=90, max_digits=6),
        ),
        migrations.AddField(
            model_name='van',
            name='daily_rate_july_to_september',
            field=models.DecimalField(decimal_places=2, default=130, max_digits=6),
        ),
        migrations.AddField(
            model_name='van',
            name='daily_rate_october_to_november',
            field=models.DecimalField(decimal_places=2, default=110, max_digits=6),
        ),
    ]