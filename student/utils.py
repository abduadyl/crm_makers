from decimal import Decimal


FIRST_PAYMENT = 200


def get_price(instance):
    discount_price = Decimal(instance.group.price - (instance.group.price * instance.discount / 100))
    return discount_price


def get_duration(instance):
    import math
    duration_month = math.floor(int(str(instance.group.end - instance.group.start).split(' ')[0]) / 30)
    return duration_month


def payment(instance):
    import math
    duration_month = math.floor(int(str(instance.group.end - instance.group.start).split(' ')[0]) / 30)
    group_price = instance.group.price # 800
    individual_price = instance.course_price
    discount = group_price - individual_price
    per_month = (group_price - FIRST_PAYMENT) / (duration_month - 1)
    print(per_month)
    last_month = per_month - discount
    
    duration_check = {
        4: per_month,
        3: per_month,
        2: per_month,
        1: last_month
    }

    if instance.duration_check in duration_check:
        return duration_check.get(instance.duration_check)
    return 0