class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, start: int, stop: int, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start
        if self.step == 0:
            raise StepValueError('Шаг не может быть равен 0')

    def __iter__(self):
        self.pointer = self.start
        self.fl = 0
        return self

    def __next__(self):
        self.pointer = self.start if self.fl == 0 else self.pointer + self.step
        self.fl = self.fl + 1

        if self.pointer > self.stop and self.step > 0:
            raise StopIteration
        elif self.pointer < self.stop and self.step < 0:
            raise StopIteration
        return self.pointer


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
for i in iter2:
    print(i, end=' ')
print()

iter3 = Iterator(6, 15, 2)
for i in iter3:
    print(i, end=' ')
print()

iter4 = Iterator(5, 1, -1)
for i in iter4:
    print(i, end=' ')
print()

iter5 = Iterator(10, 1)
for i in iter5:
    print(i, end=' ')
print()
