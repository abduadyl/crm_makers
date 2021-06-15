from decimal import Decimal


def get_price(instance):
    discount_price = Decimal(instance.group.price - (instance.group.price * instance.discount / 100))
    return discount_price


def get_duration(instance):
    import math
    duration_month = math.floor(int(str(instance.group.end - instance.group.start).split(' ')[0]) / 30)
    return duration_month


def payment(instance):
    if not instance.total_paid >= instance.course_price: # проверка для того чтобы остановить программу когда total_paid больше или равен course_price
        discount_price = instance.group.price - instance.course_price # нахождение скидки
        dict_of_all_months = {k: v for k, v in instance.group.__dict__.items() if 'payment_month' in k} # мы получаем все месяцы при создании группы
        duration_check = {k: v for k, v in dict_of_all_months.items() if v} # здесь мы фильтруем месяцы у которых есть цена
        last_month = duration_check.pop(sorted(list(duration_check.keys()))[-1]) # эта переменная для замены ключа последнего месяца на ключ last_month
        duration_check['last_month'] = last_month - discount_price # новое значение для ключа last_month в duration_check с учетом скидки
        # list_of_months = [month for month in duration_check]
        var = list(duration_check.values())[::-1][instance.duration_check-1] # мы превращаем наш словарь со значениями в лист и переварачиваем его и получаем с помощью duration_check получаем значения
        if instance.payment_month: # если студент не оплатил за определенный месяц то по логике мы должны вывести оставшуюся сумму(это должно работать при последнем месяце либо с большой скидкой)
            return instance.course_price - instance.payment_month
        if instance.credit_balance and instance.credit_balance < var: # если студент оплатил и у него в кредите осталась сумма которая превышает сумму данного месяца
            return instance.credit_balance # то мы вывыодим просто его кредит
        if instance.course_price < var: # если оплата за текущий месяц больше чем оплата за весь курс
            return instance.course_price # то мы выводим оплату за весь курс
        return var # в остальных случаях мы возвращаем значение со словаря
    return 0 # если наше условие не сработало мы возрвращаем 0 для избежания ошибки
