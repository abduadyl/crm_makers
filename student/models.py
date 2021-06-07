from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from group.models import Group
from django.db.models.signals import pre_save
from .utils import get_price


class Student(models.Model):
    personal_data = models.CharField(max_length=250, db_index=True)
    passport_ID = models.CharField(max_length=250)
    passport_INN = models.CharField(max_length=250)
    passport_date = models.DateField()
    issuing = models.CharField(max_length=250)
    phone_number = PhoneNumberField()
    email = models.EmailField()
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING, related_name='student')
    comment = models.TextField(null=True, blank=True)
    discount = models.PositiveIntegerField(default=0)
    course_price = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    payment_month = models.DecimalField(decimal_places=2, max_digits=10, default=200)
    total_paid = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    credit_balance = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    reserve = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    penalty_days = models.PositiveIntegerField(default=0)
    penalty_total = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    freeze_date = models.DateField(null=True, blank=True)
    freeze_status = models.BooleanField(default=False)
    check = models.BooleanField(default=False)
    duration_check = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created', ]

    def __str__(self):
        return self.personal_data


# Оплата за учебу с скидкой
def discount_price(sender, instance, *args, **kwargs):
    if not instance.discount:
        instance.course_price = instance.group.price
    elif instance.discount:
        instance.course_price = get_price(instance)


# Заморозка студента дата и статус
def freeze(sender, instance, *args, **kwargs):
    from datetime import datetime
    if instance.freeze_status is True:
        instance.freeze_date = datetime.now().strftime("%Y-%m-%d")


# # добавление оплаты каждый месяц
# def update_payment(sender, instance, *args, **kwargs):
#     if instance.check:
#         instance.payment_month += payment(instance)
#         instance.check = False


pre_save.connect(discount_price, sender=Student)
pre_save.connect(freeze, sender=Student)
# pre_save.connect(update_payment, sender=Student)

