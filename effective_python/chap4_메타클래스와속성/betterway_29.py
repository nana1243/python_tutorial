"""
29. getter & setter 대신에, 일반 속성을 사용하자.

- property의 단점
    1. 대응하는 메서드를 서브클래스에서만 공유 할 수 있다는 점
    2. descriptor 기능을 지원함
    ** 주의사항 : 게터 프로퍼티메서드에서 다른 속성을 설정하지 맗아야한

"""


class Resistor(object):
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0


class VoltageResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
        self._voltage = 0

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        self.current = self._voltage / self.ohms

    @property
    def ohms(self):
        # 다른 속성을 혼용해서 쓰면 안된다.
        self.voltage = self._ohms * self.current
        return self._ohms


"""
[정리]
1. 간단한 공개속성을 사용하여 새 클래스 인터페이스를 정의하고 ,
    세터와 게터 메서드는 사용하지 말자
2. 객체의 속성에 접근할때 특별한 동작을 정의하려면, @property를 사용하자

"""
