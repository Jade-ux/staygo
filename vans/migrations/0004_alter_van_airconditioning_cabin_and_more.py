# Generated by Django 4.0.1 on 2022-01-25 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vans', '0003_alter_van_mileage_limit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='van',
            name='airconditioning_cabin',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='van',
            name='airconditioning_home_area',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='van',
            name='awning',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='van',
            name='breakdown_cover',
            field=models.CharField(default='National', max_length=254),
        ),
        migrations.AlterField(
            model_name='van',
            name='camping_table_chairs',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='van',
            name='cleaning_fee',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='van',
            name='cruise_control',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='van',
            name='extras_awning',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='van',
            name='extras_bbq',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='van',
            name='extras_bike_rack',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='van',
            name='extras_chemical_toilet',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='van',
            name='extras_cutlery_crockery',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='van',
            name='extras_towbar',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='van',
            name='extras_travel_box',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='van',
            name='fuel_type',
            field=models.CharField(default='Diesel', max_length=254),
        ),
        migrations.AlterField(
            model_name='van',
            name='gas_cylinder',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='van',
            name='heating',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='van',
            name='hot_water',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='van',
            name='kitchen_equipment',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='van',
            name='motorhome_insurance',
            field=models.CharField(default='Included', max_length=254),
        ),
        migrations.AlterField(
            model_name='van',
            name='power_steering',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='van',
            name='refrigerator',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='van',
            name='seats',
            field=models.CharField(default='2', max_length=254),
        ),
        migrations.AlterField(
            model_name='van',
            name='security_deposit',
            field=models.DecimalField(decimal_places=2, default=850, max_digits=6),
        ),
        migrations.AlterField(
            model_name='van',
            name='size_description',
            field=models.CharField(default='Compact', max_length=254),
        ),
        migrations.AlterField(
            model_name='van',
            name='sleeps',
            field=models.CharField(default='2', max_length=254),
        ),
        migrations.AlterField(
            model_name='van',
            name='tv',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
