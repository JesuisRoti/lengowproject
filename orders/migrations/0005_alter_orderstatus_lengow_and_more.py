# Generated by Django 4.0.5 on 2022-06-10 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0004_alter_orderstatus_unique_together"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderstatus",
            name="lengow",
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="orderstatus",
            name="marketplace",
            field=models.TextField(null=True),
        ),
    ]
