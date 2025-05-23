# Generated by Django 5.1.3 on 2025-01-08 13:24

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("paniavault", "0009_meltpiece_code_meltpiece_is_sold_meltpiece_vitrin"),
    ]

    operations = [
        migrations.AddField(
            model_name="meltpiece",
            name="net_weight",
            field=models.DecimalField(
                decimal_places=2,
                default=Decimal("0.00"),
                max_digits=10,
                verbose_name="وزن خالص قطعه",
            ),
        ),
    ]
