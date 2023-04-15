# Generated by Django 4.2 on 2023-04-14 23:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('extraction_datetime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('movie', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='letterboxd_scraper.moviemodel')),
                ('release_year', models.IntegerField(blank=True, null=True)),
                ('poster_url', models.URLField(blank=True, null=True)),
                ('resized_poster', models.URLField(blank=True, null=True)),
                ('extraction_datetime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='StatsModel',
            fields=[
                ('movie', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='letterboxd_scraper.moviemodel')),
                ('views', models.IntegerField()),
                ('likes', models.IntegerField()),
                ('added_to_playlist', models.IntegerField()),
                ('extraction_datetime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='RecentReviewModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('review', models.TextField()),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('extraction_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='letterboxd_scraper.moviemodel')),
            ],
        ),
        migrations.CreateModel(
            name='PopularReviewModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('review', models.TextField()),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('extraction_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='letterboxd_scraper.moviemodel')),
            ],
        ),
    ]
