# Generated by Django 5.0.2 on 2024-03-07 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instruments', '0007_instrument_bio_alter_instrument_brand_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrument',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
