"""
1. python은 공유로 호출 하는 매개변수 전달 방식만 지원한다
1-1 공유로 호출 한다는 말은?
    함수의 각 매개변수가 인수로 전달받은 각 참조의 사본을 받는 다는 의미
2. 기본 자료형은 값으로 호출 하는 방식을 사용한다 : call by value

"""


def f(a, b):
    a += b
    return a


x = 1
y = 2

print(f(x, y))
print(x, y)
