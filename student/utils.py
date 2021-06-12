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
    FIRST_PAYMENT = 200
    duration_month = math.floor(int(str(instance.group.end - instance.group.start).split(' ')[0]) / 30) # count of months
    discount = instance.group.price - instance.course_price # 560 if 800, 400 if 400
    
    course_price = instance.group.price - discount # 240(800 - 560) / 400
    last_month = course_price - discount
    get_payment = (course_price - FIRST_PAYMENT) / (duration_month - 1) # ~9(240-200 / 3) / 66(400-200) / 3
    
    duration_check = {
        4: get_payment,
        3: get_payment,
        2: get_payment,
        1: last_month
    }
    
    if instance.duration_check in duration_check:
        if instance.course_price <= 200:
            return instance.course_price

        if get_payment <= 100:
            instance.duration_check = 2
            instance.payment_month = get_payment
            return duration_check.get(instance.duration_check)

        return duration_check.get(instance.duration_check)

    return 0