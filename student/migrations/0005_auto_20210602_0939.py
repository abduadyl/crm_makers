# Generated by Django 3.1 on 2021-06-02 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20210602_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]