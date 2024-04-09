# Generated by Django 5.0.2 on 2024-03-07 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instruments', '0010_alter_instrument_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrument',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, null=True),
        ),
    ]
