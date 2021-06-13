from decimal import Decimal


def get_price(instance):
    discount_price = Decimal(instance.group.price - (instance.group.price * instance.discount / 100))
    return discount_price


def get_duration(instance):
    import math
    duration_month = math.floor(int(str(instance.group.end - instance.group.start).split(' ')[0]) / 30)
    return duration_month


def payment(instance):
    import math
    if not instance.payment_month == instance.course_price:
        duration_month = math.floor(int(str(instance.group.end - instance.group.start).split(' ')[0]) / 30) # count of months    
        discount_price = instance.group.price - instance.course_price
        dict_of_all_months = {k: v for k, v in instance.group.__dict__.items() if 'payment_month' in k}
        duration_check = {k: v for k, v in dict_of_all_months.items() if v}
        if instance.course_price < duration_check.get('payment_month_1'):
            duration_check['payment_month_1'] = instance.course_price
            return list(duration_check.values())[::-1][instance.duration_check-1]
        last_month = duration_check.pop(sorted(list(duration_check.keys()))[-1])
        duration_check['last_month'] = last_month - discount_price
        return list(duration_check.values())[::-1][instance.duration_check-1]