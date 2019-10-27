# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        self.cur = -1
        if len(kwargs) < 1:
            self.ignore_case = False
        else:
            self.ignore_case = kwargs['ignore_case']

        if len(kwargs) < 1 or kwargs['ignore_case'] is False:
            self.list = list({x for x in items})
        else:
            tmp = {}
            for x in items:
                if tmp.get(str(x).lower()) is None:
                    tmp[str(x).lower()] = str(x)
            self.list = list(tmp.values())

    def __next__(self):
        if self.cur + 1 < len(self.list):
            self.cur += 1
            return self.list[self.cur]
        else:
            raise StopIteration
        # Нужно реализовать __next__

    def __iter__(self):
        return self
