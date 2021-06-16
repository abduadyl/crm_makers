# Generated by Django 3.1 on 2021-05-29 18:14

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personal_data', models.CharField(max_length=250)),
                ('passport_ID', models.CharField(max_length=250)),
                ('passport_INN', models.CharField(max_length=250)),
                ('passport_date', models.DateField()),
                ('issuing', models.CharField(max_length=250)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.TextField()),
                ('discount', models.PositiveIntegerField(default=0)),
                ('course_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('payment_month', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total_paid', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('credit_balance', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('reserve', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='student', to='group.group')),
            ],
        ),
    ]
