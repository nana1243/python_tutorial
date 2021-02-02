import copy
from copy import deepcopy

"""
1. copy() 와 deepcopy() 를 이용해서 세개의 bus 객체를 생성한다
"""


class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


bus1 = Bus(["a1", "a2", "a3"])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)

print(f"bus1_id : {id(bus1)} && bus2_id : {id(bus2)} && bus3_id : {id(bus3)}")

bus1.drop("a1")
print(bus2.passengers)
print(bus3.passengers)


"""
객체 안에 참조가 있으면 단순한 알고리즘은 무한 루프에 빠질 수 있다
"""

a = [10, 20]
b = [a, 30]
a.append(b)
print(a)


c = deepcopy(a)
print(c)
