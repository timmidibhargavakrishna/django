# Generated by Django 2.2 on 2019-05-08 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('booking_title', models.CharField(max_length=50)),
                ('booking_type', models.CharField(max_length=20)),
                ('booking_date', models.CharField(max_length=10)),
                ('booking_description', models.CharField(max_length=500)),
            ],
        ),
    ]