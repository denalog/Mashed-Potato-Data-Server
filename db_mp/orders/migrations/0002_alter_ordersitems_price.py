# Generated by Django 5.1.3 on 2025-01-10 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordersitems',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]