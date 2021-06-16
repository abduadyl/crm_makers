# Generated by Django 3.1 on 2021-06-12 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0002_auto_20210530_1804'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bill',
            old_name='total',
            new_name='penalty_total',
        ),
        migrations.RemoveField(
            model_name='bill',
            name='payment_type',
        ),
        migrations.AddField(
            model_name='bill',
            name='study_total',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
    ]
