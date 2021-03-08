"""
Better way 14:None을 반환하기 보다는 예외를 일으키자
-  None다을 반환할 경우 함수가 오류를 일으키기 쉬운 이유는 0이나 빈 문자열이 조건식에 False
    로평가하기 때문이다
- 특별한 상황을 알릴 때 None을 반환하는 대신에 예외를 일으키자

"""


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


# tuple을 통해서 이를 해결한다
# 문제는 호출자가 (파이썬에서 사용하지 않는 변수에 붙이는 관례인 밑줄 변수 이름을 사용해서) 튜플의 첫번째 부분을
# 쉽게 무시할 수 있다
def divide_1(a, b):
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None


def divide_2(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError("Invalid inputs!") from e


result = divide(0, 1)

if result is not None:
    print("Invalid inputs!")
else:
    print("Not Invalid inputs!")
print(result)


result2 = divide_2(0, 0)
print(result2)
