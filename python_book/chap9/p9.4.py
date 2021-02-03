"""
@classmethod 와 @staticmethod

@classmethod
    - 호출되는 방식을 변경해서 클래스 자체를 첫번째 인수로 받게 만들며,
        frombytes() 같은 대안 생성자를 구현하기 위해 주로 사용

@staticmethod
    - 메소드가 특별한 첫번째 인수를 받지 않도록 메서드를 변경한다

NOTE
    - @classmethod 데커레이터는 쓰임새가 많은 건 확실하지만, @staticmethod 사용해야 하는 이유를 잘 모르겟다
        - 클래스와 함께 작동하지 않는 함수를 구현하려면, 단지 함수를 모듈에 정의하면 된다
        - 아마, 함수가 클래스를 건들이지는 않지만, 그 클래스와 밀접히 연관되어 잇어서 클래스 코드 가까운 곳에 두고 싶을 수는 있다
        - 그런 경우, 클래스의 바로 앞이나 뒤에서 함수를 정의하면 된다.
"""


class Demo:
    @classmethod
    def klassmeth(cls, *args):
        return args

    @staticmethod
    def statmeth(*args):
        return args


print(Demo.klassmeth())
print(Demo.klassmeth("spam"))
print(Demo.statmeth())
print(Demo.statmeth("spam"))
