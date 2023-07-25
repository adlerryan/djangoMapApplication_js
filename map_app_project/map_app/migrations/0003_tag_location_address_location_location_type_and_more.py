# Generated by Django 4.2.3 on 2023-07-23 14:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("map_app", "0002_remove_location_image_location_cover_charge_review_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name="location",
            name="address",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="location",
            name="location_type",
            field=models.CharField(
                choices=[
                    ("bar", "Bar"),
                    ("brewery", "Brewery"),
                    ("club", "Club"),
                    ("winebar", "Wine Bar"),
                ],
                default=11,
                max_length=10,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="location",
            name="phone_number",
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="location",
            name="lat",
            field=models.DecimalField(decimal_places=6, max_digits=25),
        ),
        migrations.AlterField(
            model_name="location",
            name="lng",
            field=models.DecimalField(decimal_places=6, max_digits=25),
        ),
        migrations.AddField(
            model_name="location",
            name="tags",
            field=models.ManyToManyField(related_name="locations", to="map_app.tag"),
        ),
    ]
