# Generated by Django 4.0.5 on 2022-06-10 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0003_order_order_status"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="orderstatus",
            unique_together={("marketplace", "lengow")},
        ),
    ]
