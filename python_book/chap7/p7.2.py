registry = []  # @register로 데코레이터된 함수들에 대한 참조를 담는다


def register(func):  # 함수를 인수로 받는다
    print("running register(%s)" % func)  # 데코레이터된 함수를 출력한다
    registry.append(func)  # func를 registery에 추가한다
    return func


@register
def f1():
    print("running f1()")


@register
def f2():
    print("running f2()")


def f3():
    print("running f3()")


def main():  # f1(),f2(),f3() 차례대로 호출한다
    print("running main()")
    print("registry -> ", registry)
    f1()
    f2()
    f3()


if __name__ == "__main__":
    main()  # p7.2를 스크립트로 실행할만 호출된다
