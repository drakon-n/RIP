# Здесь необходимо реализовать
# контекстный менеджер timer
# Он не принимает аргументов, после выполнения блока он должен вывести время выполнения в секундах
# Пример использования
# with timer():
#   sleep(5.5)
#
# После завершения блока должно вывестись в консоль примерно 5.5
import contextlib
from time import time


@contextlib.contextmanager
def timer():
    time_now = time()
    yield
    print(format(time() - time_now, '.10f'))