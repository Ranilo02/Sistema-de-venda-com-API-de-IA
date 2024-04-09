# Generated by Django 5.0.2 on 2024-03-07 11:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instruments', '0006_instrumentinventory'),
    ]

    operations = [
        migrations.AddField(
            model_name='instrument',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='instrument',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='instrument_brand', to='instruments.brand'),
        ),
        migrations.AlterField(
            model_name='instrument',
            name='model',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='instrument',
            name='product',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
