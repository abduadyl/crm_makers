# Generated by Django 3.1 on 2021-06-10 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0018_auto_20210607_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='payment_month',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
