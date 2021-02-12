import abc

"""
ABC의 정의와 사용
- ABC를 생성하는 일을 정당화하기 위해, 프레임워크를 확장해야 한느 상황을
    만들어 보자
    - ADAM : 광고 관리 프레임워크를 만든다고 가정
    - `무반복 무작위 선택` 요소가 갖추어야 할 성질을 명확히 알려주기 위해 ABC 사용
"""


class Tombola(abc.ABC):  # ABC를 정의하려면, abc.ABC를 상속해야한다
    """
    이 코드의 핵심 : ABC안에서 인터페이스에 정의된 다른 메서드만 이용하는 한 A
    ABC에 구상 메서드를 제공하는것도 가능하다는 점
    """

    @abc.abstractmethod
    def load(self, iterable):
        pass
        """iteralbe의 항목을 추가한다"""

    @abc.abstractmethod
    def pick(self):
        """무작위로 항목 하나를 제거하고 반환한다.
        객체가 비어 있을 때, 메서드를 실행하면  `LookupError` 발생한다.
        """

    def loaded(self):  # ABC의 구상메서드가 들어 갈 수 있다
        """최소 한개 항목이 있으면 True, 아니면 False"""
        return bool(self.inspect())

    def inspect(self):  # ABC 구상메스드는 반드시 ABC에 정의된 인터페이스만 사용해야한다
        """현재 안에 항목들로 구성된 정렬 튜플을 반환"""
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))
