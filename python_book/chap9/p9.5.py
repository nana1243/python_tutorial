import math
from array import array
from datetime import datetime

"""
포맷된 출력

format()
    - format() 내장 함수와 str.format() 메소드는 실제 포맷 작업을 #noqa:W291
        __format__(format_spec) 메서드를 위임한다
    - format_spec 포맷 명시자로써 , 다음 두 가지 방법 중 하나를 통해 지정
        - 1. fomrat(my_obeject, format_spec)
        - 2. str.format(rate : 필드먕)
"""

brl = 1 / 2.43
print(brl)
print(format(brl, "0.4f"))
print("1 BRL = {rate:0.2f} USD ".format(rate=brl))
print(format(42, "b"))

"""
각 클래스가 format_spec 인수를 자신이 원하는 대로 해석해서, 포맷 명시간이 언어를 확장 할 수 있다
"""


now = datetime.now()
format(now, "%H : %M : %S")
print("It's now {:%I :%M %p}".format(now))


class Vector2d:
    typecode = "d"

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):  # Vector2d를 반복할 수 있도록 도와준다
        return (i for i in range(self.x, self.y))

    def __repr__(self):  # 문자열로 치환해 문자열을 만든다
        class_name = type(self).__name__
        return "{}(){!r},{!r}".format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes[ord(self.typecode)] + bytes(array(self.typecode, self))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):  # 객체의 크기를 반환
        return math.hypot(self.x, self.y)

    def __bool__(self):  # 크기가
        return bool(abs(self))

    def __format__(self, format_spec=""):
        components = (format(c, format_spec) for c in self)
        return "({},{})".format(*components)

    def angle(self):
        return math.atan2(self.y, self.x)

    def __format2__(self, format_spec=""):  # version-2
        if format_spec.endswith("p"):
            format_spec = format_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = "<{},{}>"
        else:
            coords = self
            outer_fmt = "({},{})"
        components = (format(c, format_spec) for c in coords)
        return outer_fmt.format(*components)

    @classmethod  # class method에는 데커레이터가 붙는다
    def frombytes(cls, octets):  # self 변수가 없다. 대신 클래스 자신이 cls 매개변수로 전달된다
        typecode = chr(octets[0])  # 첫번째 바이트에서 typecode를 읽는다
        memv = memoryview(
            octets[1:].cast(typecode)
        )  # octets 이진 시퀀스로부터 memoryview를 생성하고 typecode를 이용해서 형을 변환한다
        return cls(*memv)  # cast()가 반환한 memoryview를 언패킹해서 생성자에게 필요한 인수로 전달한다


v1 = Vector2d(3, 4)
print(format(v1))
