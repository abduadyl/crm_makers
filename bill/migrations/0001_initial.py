# Generated by Django 3.1 on 2021-06-16 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usd', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('kgs', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('eur', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('study_total', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('penalty_days', models.PositiveIntegerField(default=0)),
                ('penalty_total', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('payment_choice', models.CharField(choices=[('cash', 'Наличные'), ('elsom', 'Эльсом'), ('card', 'Карта')], max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='bills', to='student.student')),
            ],
        ),
    ]
