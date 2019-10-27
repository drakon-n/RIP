import random


# Генератор вычленения полей из массива словарей
# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(items, *args):
    assert len(args) > 0, 'Enter arguments'
    if len(args) == 1:
        tmp = []
        for x in items:
            try:
                value = x[args[0]]
            except KeyError as e:
                print("Wrong key in args: '{}'".format(e.args[0]))
                return
            if not (value is None):
                tmp.append(value)
    else:
        tmp = []
        for x in items:
            try:
                tmp.append({key: x[key] for key in args if not (x[key] is None)})
            except KeyError as e:
                print("Wrong key in args: '{}'".format(e.args[0]))
                return
    return tmp




# Генератор списка случайных чисел
# Пример:
# gen_random(1, 3, 5) должен выдать примерно 2, 2, 3, 2, 1
# Hint: реализация занимает 2 строки
def gen_random(begin, end, num_count):
    return list([random.randint(begin, end) for x in range(num_count)])
    # Необходимо реализовать генератор
