# Generated by Django 2.1.2 on 2019-03-14 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_payment', '0003_auto_20190314_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_date',
            field=models.CharField(max_length=10),
        ),
    ]