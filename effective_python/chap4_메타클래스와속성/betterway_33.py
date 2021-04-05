"""
33. 메타 클래스로 서브 클래스를 검증하자
    - 메타 클래스를 응용하는 가장 간단한 사례는 서브클래스를 검증하는 것이다
    - 보통 검증 코드는 __init__ 이 실행될때 ,실행된다
    - 서브클래스 검증용으로 메타클래스를 정의하는 방법을 알기 위해, 메타클래스가 표준 객체에는 어떻게 동작하는지 이해해야한다.

    - 정리
        - 서브클래스 타입의 객체를 생성하기 앞서 서브클래스가 정의 시점부터 제대로 구성되었음을 보장하려면, 메타 클래스를 사용
        - 메타클래스의 __new__ 메서드는 class 문의 본문 전체가 처리된 후에 실행한다
"""


class Meta(type):
    def __new__(meta, name, bases, class_dict):
        print(type(meta, name, bases, class_dict))
        return type.__new__(meta, name, bases, class_dict)


# 메타클래스는 클래스가 상속하는 부모 클래스 및 class에서 정의한
# 모든 클래스 속성에 접근 가능


class MyClass(object, metaclass=Meta):
    stuff = 123

    def foo(self):
        pass


# 클래스가 정의되기전에 클래스의 모든 파라미터를 검증하려면 Meta.__new__메서드에 기능 추가
# ex) 여러 면으로 이루어진 다각형을 어떤 타입이든 표현하고자함
# 이렇게 하려면, 다각형 클래스 계층의 기반 클래스에 사용하면 된다.
# 이때 기반 클래스에는 같은 검증을 적용하지 말아야 한다는 점을 유의하기 바란다.


class ValidatePolygon(type):
    def __new__(meta, name, bases, class_dict):
        if bases != (object,):
            if class_dict["sides"] < 3:
                raise ValueError("Polygons need 3+ sides")
        return type.__new__(meta, name, bases, class_dict)


class Polygon(object, metaclass=ValidatePolygon):
    sides = None

    @classmethod
    def interior_angles(cls):
        return (cls.sides - 2) * 180


# 면이 세 개 미만인 다각형을 정의하려고 하면 검증 코드가 실패!
