# Generated by Django 5.1.3 on 2025-05-13 19:34

import django_jalali.db.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("paniavault", "0025_piecetransfer"),
    ]

    operations = [
        migrations.AddField(
            model_name="piecetransfer",
            name="is_received",
            field=models.BooleanField(
                default=False, verbose_name="تأیید شده توسط گیرنده؟"
            ),
        ),
        migrations.AddField(
            model_name="piecetransfer",
            name="is_sent",
            field=models.BooleanField(
                default=False, verbose_name="ارسال شده توسط فرستنده؟"
            ),
        ),
        migrations.AddField(
            model_name="piecetransfer",
            name="received_at",
            field=django_jalali.db.models.jDateTimeField(
                blank=True, null=True, verbose_name="زمان دریافت"
            ),
        ),
        migrations.AddField(
            model_name="piecetransfer",
            name="sent_at",
            field=django_jalali.db.models.jDateTimeField(
                blank=True, null=True, verbose_name="زمان ارسال"
            ),
        ),
    ]
