"""
32. 지연속성에는 __getattr__ , __getattribute__, __setattr__를 사용하자

    - 지연 평가란?
        파이썬에서는 이터레이터만 생성하고 값이 필요한 시점이 되었을 때 값을 만드는 방식을 사용합니다.
        즉, 데이터 생성을 뒤로 미루는 것인데 이런 방식을 지연 평가(lazy evaluation)

    `__getattr__` :
        - 파이썬에는 객체와 데이터베이스를 연결하는 코드에서 로우의 스키마를 몰라도 된다
        - `__getattr__` 이라는 특별한 메소드로 이런 동작을 가능하게 한다.
        - 클래스에서 , __getattr__ 메서드를 정의하면, 인스턴스 딕셔너리에서 속성을 찾을 수 없을떄 마다
        이 메소드가 호출된다.

    `__getattribute__` :
        - 객체의 속성에 접근할 때마다 호출되며, 심지어 해당 속성이 속성 딕셔너리에 있을 때도 호출

    - [정리]
    • __getattr__은 존재하지 않는 속성에 접근할 때 한 번만 호출되는
        반면에 __getattribute__는 속성에 접근할 때마다 호출된다는 점을 이해하자.
    • __getattribute__와 __setattr__에서 인스턴스 속성에 직접 접근할 때
     super()(즉, object 클래스)의 메서드를 사용하여 무한 재귀가 일어나지 않게 하자.
"""


class LazyDB(object):
    def __init__(self):
        self.exists = 5

    def __getattr__(self, name):
        value = "Value for %s" % name
        setattr(self, name, value)
        return value

    def __getattribute__(self, name):
        print("Called__getattribute__( % s)" % name)
        try:
            return super().__getattribute__(name)
        except AttributeError:
            value = "Value for % s% name"
            setattr(self, name, value)
            return value


data = LazyDB()
print("Before : ", data.__dict__)
# 존재하지 않는 속성인 foo 에 접근해보자
print("foo : ", data.foo)
print("After :", data.__dict__)


class SaveDB(object):
    def __setattr__(self, name, value):
        super().__setattr__(name, value)


class LoggingSaveDb(SaveDB):
    def __setattr__(self, name, value):
        print("Called__setattribute__( % s %s)" % name % value)
