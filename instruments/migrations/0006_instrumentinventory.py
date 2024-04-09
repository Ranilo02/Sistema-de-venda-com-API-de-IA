# Generated by Django 5.0.2 on 2024-03-07 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instruments', '0005_alter_instrument_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstrumentInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instruments_count', models.IntegerField()),
                ('instruments_value', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]