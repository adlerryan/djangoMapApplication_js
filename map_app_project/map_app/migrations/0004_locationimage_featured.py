# Generated by Django 4.2.3 on 2023-07-23 15:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("map_app", "0003_tag_location_address_location_location_type_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="locationimage",
            name="featured",
            field=models.BooleanField(default=False),
        ),
    ]