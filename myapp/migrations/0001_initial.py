# Generated by Django 3.2.9 on 2021-12-18 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HikeMeUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, verbose_name='User Email')),
            ],
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=50, verbose_name='Location Name')),
                ('location_description', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='HikeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hike_name', models.CharField(max_length=50)),
                ('hike_description', models.TextField(blank=True, max_length=200)),
                ('hike_difficulty', models.CharField(blank=True, default='hard', max_length=50)),
                ('hike_hikers', models.ManyToManyField(blank=True, to='myapp.HikeMeUsers')),
                ('hike_location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.locations')),
            ],
        ),
    ]
