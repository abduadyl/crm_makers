# Generated by Django 3.1 on 2021-06-03 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_auto_20210603_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
