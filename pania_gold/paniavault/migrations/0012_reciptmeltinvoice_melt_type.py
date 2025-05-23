# Generated by Django 5.1.3 on 2025-01-09 03:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("paniavault", "0011_reciptmeltinvoice_invoice_serial_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="reciptmeltinvoice",
            name="melt_type",
            field=models.CharField(
                blank=True,
                choices=[("raw", "تهاترباخام"), ("scrap", "تهاترباقیچی")],
                max_length=50,
                null=True,
                verbose_name="نوع آبشده",
            ),
        ),
    ]
