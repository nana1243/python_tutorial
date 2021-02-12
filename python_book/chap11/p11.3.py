import collections
from random import shuffle

"""
런타임에 프로토콜을 구현하는 멍키 패칭
- 시퀀스처럼 작동하는 FrenchDeck 클래스라면, shuffle()을 직접 구현할 필요가 없다

멍키패칭
- 소스코드를 건들이지 않고, 런타임에 클래스나 모듈을 변경하는 행

덕타이핑
- 객체가 어떤 프로토콜을 구현하는 한 자료형에 상관없이 객체를 작동시키는 것

"""

list1 = list(range(10))
shuffle(list1)
print(list1)

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JOKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [
            Card(rank, suit) for suit in self.suits for rank in self.ranks
        ]  # noqa: E501

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, pos):
        return self._cards[pos]


deck = FrenchDeck()
# shuffle함수는 컬렉션 안의 교환시킴으로써 작동하는데, FrenchDeck는 불변 시퀀스 프로토콜만 구현
# 불변 시퀀스는 __setitem__()으로 구현
# TypeError: 'FrenchDeck' object does not support item assignment
shuffle(deck)


def set_card(deck, position, card):
    deck._cards[position] = card


# _setitem_이라는 이름의 속성을 할당한다
FrenchDeck.__setitem__ = set_card
shuffle(deck)
print(deck[:4])
