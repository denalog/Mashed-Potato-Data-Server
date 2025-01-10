# Generated by Django 5.1.3 on 2025-01-09 08:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("car", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CarCategory",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("category", models.CharField(max_length=30, null=True)),
                (
                    "car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="categories",
                        to="car.car",
                    ),
                ),
            ],
            options={
                "db_table": "car_category",
            },
        ),
    ]
