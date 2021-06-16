from django.db import models
from django.db.models.signals import pre_save
from student.models import Student
from .utils import get_total


class Bill(models.Model):
    PAYMENT_CHOICE = (
        ('cash', 'Наличные'),
        ('elsom', 'Эльсом'),
        ('card', 'Карта')
    )
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING, related_name='bills')
    usd = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    kgs = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    eur = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    study_total = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    penalty_days = models.PositiveIntegerField(default=0)
    penalty_total = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    payment_choice = models.CharField(max_length=50, choices=PAYMENT_CHOICE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.personal_data} ${self.total}"


def total_payment_study(sender, instance, *args, **kwargs):
    if not instance.study_total:
        instance.study_total = get_total(instance)


pre_save.connect(total_payment_study, sender=Bill)
