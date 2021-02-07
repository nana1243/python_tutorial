from datetime import date

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
        - 가장 큰 차이점은 상태를 바꿀수 있냐(cls method) 없냐(static method)(from geek)
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


"""
Geeks
    관련문서 :https://www.geeksforgeeks.org/class-method-vs-static-method-python/
    classmethod #noqa: W291
    - It can modify a class state that would apply across #noqa:W291
        all the instances of the class. #noqa:W291
        For example it can modify a class variable that will be applicable
         to all the instances
    staticmethod
    - A static method is also a method which is bound to #noqa:W291
        the class and not the object of the class.
    - A static method can’t access or modify class state.
    - It is present in a class because it makes sense for #noqa:W291
        the method to be present in class.
"""

# Python program to demonstrate
# use of class method and static method.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        # a class method to create a Person object by birth year.

    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year + 1)

        # a static method to check if a Person is adult or not.

    @staticmethod
    def isAdult(age):
        return age > 18


person1 = Person("mayank", 21)
person2 = Person.fromBirthYear("mayank", 1992)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(22))
