"""
10.2 VECTOR 버전 #1 : Vector2d 호환
    - reprlib.repr() :
        생략기호를 이용해서 생성할 문자열의 길이를 제한하므로 대형 구조체
        or 재귀적 구조체도 안전하게 표현
"""

import math
import reprlib
from array import array


class Vector:
    typecode = "d"

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        return "Vector({})".format(components)

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

    @classmethod  # class method에는 데커레이터가 붙는다
    def frombytes(cls, octets):  # self 변수가 없다. 대신 클래스 자신이 cls 매개변수로 전달된다
        typecode = chr(octets[0])  # 첫번째 바이트에서 typecode를 읽는다
        memv = memoryview(
            octets[1:].cast(typecode)
        )  # octets 이진 시퀀스로부터 memoryview를 생성하고 typecode를 이용해서 형을 변환한다
        return cls(*memv)  # cast()가 반환한 memoryview를 언패킹해서 생성자에게 필요한 인수로 전달한다
