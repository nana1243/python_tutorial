class Average:
    def __init__(self):
        self.series = []

    def __call__(self, new_value, *args, **kwargs):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


avg = Average()

t1 = avg(10)
print(t1)
t2 = avg(11)
print(t2)


"""make_average() 이동 평균을 계산"""


def make_averager():
    """ make_averager() 호출되면 averager() 함수가 호출된"""
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


avg = make_averager()
t3 = avg(10)
print(t3)

t4 = avg(11)
print(t4)


print(avg.__code__.co_varnames)
print(avg.__code__.co_freevars)
