# Generated by Django 5.1.3 on 2025-01-09 06:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "paniavault",
            "0013_companyvault_vitrin_type_alter_meltpiece_invoice_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="reciptcraftinvoice",
            old_name="serial",
            new_name="invoice_serial",
        ),
        migrations.RenameField(
            model_name="reciptcraftinvoice",
            old_name="gold_type",
            new_name="pay_type",
        ),
    ]
