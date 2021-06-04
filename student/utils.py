from decimal import Decimal


FIRST_PAYMENT = 200


def get_price(instance):
    discount_price = Decimal(instance.group.price - (instance.group.price * instance.discount / 100))
    return discount_price


# def payment(instance):
#     import math
#     duration_month = math.floor(int(str(instance.group.end - instance.group.start).split(' ')[0]) / 30)
#     instance.duration_check = duration_month
#     group_price = instance.group.price
#     individual_price = instance.course_price
#     discount = group_price - individual_price
#     per_month = (group_price - FIRST_PAYMENT) / (duration_month - 1)
#     last_month = per_month - discount
#     if instance.duration_check == 4:
#         return per_month
#     elif instance.duration_check == 3:
#         return per_month
#     elif instance.duration_check == 2:
#         return per_month
#     elif instance.duration_check == 1:
#         return last_month
#     return 0