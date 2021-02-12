"""
파이썬 문화에서의 인터페이스와 프로토콜
    - 보호된 속성과 비공개 속성은 인터페이스에 속하지 않는다고 정의
    - 공개 데이터 속성을 인터페이스로 사용하는 것은 나쁘지 않다

인터페이스
    -시스템에서 어떤 역할을 할 수 있게 해주는 객체의 공개 메서드의 일부
    - 특정 클래스를 지정하지 않고  `file과 같은 객체` or `반복형`
    - 어떤 역할을 완수하기 위한 메소드 집합으로서 인터페이스를 스몰토크에서는 `프로토콜`라고 불림
        -프로토콜은 상속과 무관
        - 클래스는 여러 프로토콜을 구현해서 객체가 여러 역할을 할 수 있게 함

프로토콜
    - 시퀀스 프로토콜은 파이썬에서 가장 핵심적인 인터페이스 중 하나이다

"""


class Vector2d:
    """x,y는 공개 데이터 속성이"""

    typecode = "d"

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in range(int(self.x), int(self.y)))


# 프로퍼티로 다시 구현한 Vector2d


class Vector2d:  # noqa : F811
    typecode = "d"

    def __init__(self, x, y):
        self._x = float(x)
        self._y = float(y)

    @property
    def x(self):
        return self._x

    def y(self):
        return self._y

    def __iter__(self):
        return (i for i in range(int(self.x), int(self.y)))
