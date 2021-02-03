"""
"""
import math
from array import array


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

    def __bytes__(self):
        return bytes[ord(self.typecode)] + bytes(array(self.typecode, self))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):  # 객체의 크기를 반환
        return math.hypot(self.x, self.y)

    def __bool__(self):  # 크기가
        return bool(abs(self))
