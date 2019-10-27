#!/usr/bin/env python3
import json
import sys
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import Unique as unique

try:
    path = sys.argv[1]
except IndexError as e:
    print('Enter path to json')
    raise SystemExit

# Здесь необходимо в переменную path получить
# путь до файла, который был передан при запуске

try:
    with open(path) as f:
        data = json.load(f)
except FileNotFoundError as e:
    print('Wrong path')
    raise SystemExit


# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Важно!
# Функции с 1 по 3 дожны быть реализованы в одну строку
# В реализации функции 4 может быть до 3 строк
# При этом строки должны быть не длиннее 80 символов

@print_result
def f1(arg):
    return field(arg, 'job-name')


@print_result
def f2(arg):
    return list(filter(lambda item: True if str(item).startswith('программист') else False, arg))


@print_result
def f3(arg):
    return list(map(lambda item: item + ' с опытом Python', arg))


@print_result
def f4(arg):
    tmp = list(zip(arg, gen_random(100000, 200000, len(arg))))
    return ['{}, зарплата {} руб.'.format(str(key), str(value)) for key, value in tmp]


with timer():
    f4(f3(f2(f1(data))))