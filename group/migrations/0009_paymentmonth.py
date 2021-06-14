# Generated by Django 3.1 on 2021-06-12 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0008_auto_20210607_2119'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMonth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.PositiveIntegerField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='payment_months', to='group.group')),
            ],
        ),
    ]
