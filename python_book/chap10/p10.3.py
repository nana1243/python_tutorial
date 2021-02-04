"""
10.3 프로토콜과 덕 타이핑
    - 객체지향 프로그래밍에서 프로토콜은 문서에만 정의되어 있고, 실제 코드에서는
        정의되지 않는 비공식 인터페이스이다
    ex) __len()__ 과 __getitem()__ 메서드를 동반할 뿐이

    - **아래 클래스(FrenchDeck)가 시퀀스 처럼 동작한다는 사실이 중요**
    - 덕 타이핑

"""

import collections

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JOKA")
    suits = "spades diamonds clubs hears".split()

    def __init__(self):
        self._card = [
            Card(rank, suit) for suit in self.suits for rank in self.ranks
        ]  # noqa:E501

    def __len__(self):
        return len(self._card)

    def __getitem__(self, position):
        return self._card[position]
