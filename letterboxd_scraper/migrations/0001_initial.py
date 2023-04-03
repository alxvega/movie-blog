# Generated by Django 4.2 on 2023-04-03 12:17

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ImageModel",
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
                ("release_year", models.IntegerField(null=True)),
                ("poster_url", models.CharField(max_length=255, null=True)),
                ("resized_poster", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="MovieModel",
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
                ("title", models.CharField(max_length=255)),
                ("slug", models.CharField(max_length=255)),
                ("rating", models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="PopularReviewModel",
            fields=[
                (
                    "review_id",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=255)),
                ("review", models.TextField()),
                ("rating", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="RecentReviewModel",
            fields=[
                (
                    "review_id",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=255)),
                ("review", models.TextField()),
                ("rating", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="StatsModel",
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
                ("views", models.IntegerField()),
                ("likes", models.IntegerField()),
                ("added_to_playlist", models.IntegerField()),
            ],
        ),
    ]
