from django.db import models
from django.db.models.signals import pre_save
from student.models import Student
from .utils import get_total


class Bill(models.Model):
    TYPE = (
        ('study', 'Оплата за обучение'),
        ('penalty', 'Оплата за пеню')
    )
    PAYMENT_CHOICE = (
        ('cash', 'Наличные'),
        ('elsom', 'Эльсом'),
        ('card', 'Карта')
    )
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING, related_name='bills')
    usd = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    kgs = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    eur = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    penalty_days = models.PositiveIntegerField(default=0)
    payment_type = models.CharField(max_length=50, choices=TYPE)
    payment_choice = models.CharField(max_length=50, choices=PAYMENT_CHOICE)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.personal_data} ${self.total}"


def total_payment(sender, instance, *args, **kwargs):
    if not instance.total:
        instance.total = get_total(instance)


pre_save.connect(total_payment, sender=Bill)
