class HauntedBus:
    """유령 승객이 출몰하는 버스 모델"""

    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


"""
1. 명시적인 승객 리스트로 초기화 되지 않은 BUS 객체들이 승객 리스트를 공유하게 되는 문제가 발생한다
2. 기본값은 수 객체의 속성이 된다
3. 따라서, 기본값이 가변 객체이고 이 객체를 변경하면 변경 내요이 향ㅎ에 이 함수의 호출에 영향을 준다

[결론] : 가변 기본값에 대한 이러한 문제 때문에 passengers 인수가 None인지 확인하고
        새로 만든 빈 리스트를 passengers에 할당한다
"""

h1 = HauntedBus(["a", "b", "c"])
h1.pick("d")
print(h1.passengers)

h2 = HauntedBus()
h2.pick("hennie")
print(h2.passengers)

h3 = HauntedBus()
print(h3.passengers)

print(dir(HauntedBus.__init__))
print(dir(HauntedBus.__init__.__defaults__))
print(dir(HauntedBus.__init__.__defaults__[0]) is h3.passengers)
