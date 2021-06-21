from typing import Tuple
from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_title_generator


class Time(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True

        
class PaymentMonth(models.Model):
    payment_month_1 = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    payment_month_2 = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    payment_month_3 = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    payment_month_4 = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    payment_month_5 = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    payment_month_6 = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    payment_month_7 = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    payment_month_8 = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    payment_month_9 = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    payment_month_10 = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    payment_month_11 = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    payment_month_12 = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)

    class Meta:
        abstract = True


class Course(Time):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title


class Group(PaymentMonth, Time):
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, related_name='course')
    title = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    start = models.DateField()
    end = models.DateField()
    total_students = models.PositiveIntegerField(default=0)
    last_check = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at', ]

    def __str__(self):
        return self.title


def title_generator(sender, instance, *args, **kwargs):
    instance.title = unique_title_generator(instance)


pre_save.connect(title_generator, sender=Group)


