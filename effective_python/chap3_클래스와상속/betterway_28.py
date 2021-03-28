"""
커스텀 컨테이너 타입은 collections.abc 의 클래스를 상속받게 하자
"""


class BinaryNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# 파이썬은 특별한 이름을 붙인 인스턴스 메서드로 컨테이너 동작을 구현

bar = [1, 2, 3]
print(bar.__getitem__(0))

# BinaryNode 클래스가 시퀀스처럼 동작하게 하려면 객체의 트리를 깊이 우선으로 탐색하는 __getitem__을 구현하면 된다.


class IndexableNode(BinaryNode):
    def _search(self, count, index):
        found, count = False, 0
        return found, count

    def __getitem__(self, item):
        found, _ = self._search(0, 0)

        if not found:
            raise IndexError("Index out of range")
        return found.value


# 그러나, __getitem__을 구현하는 것만으로는 기대하는
# 시퀀스 시맨틱을 모두 제공하지 못한다는 점이다.

"""
파이썬 세계의 이런 어려움을 피하려고 내장 collections.abc 모듈은
각 컨테이너 타입에 필요한 일반적인 메서드를 모두 제공하는
추상 기반 클래 스들을 정의한다.
이 추상 기반 클래스들에서 상속받아 서브클래스를 만들다가 깜빡 잊고
필수 메서드를 구현하지 않으면, 모듈이 뭔가 잘못되었다고 알려준다.
[결론]
1. 쓰임새가 간단할때는 list, dict 같은 파이썬 컨테이너 타입에서 직접 상속받게하자
2. 커스텀 컨테이너 타입을 올바르게 구현하는데 필요한 많은 메서드에 주의해야하다
3. 커스텀 컨테이너 타입이 collections.abc에 정의된 인터페이스에서 상속받게 만들어서
클래스가 필요한 인터페이스 ,동작을 일치하게 하자
"""
