# Generated by Django 3.1 on 2021-06-03 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_auto_20210603_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
    ]