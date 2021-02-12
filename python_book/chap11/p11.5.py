import collections

"""
ABC 상속하기
- 파이썬은 모듈을 로딩하거나, 컴파일 할때가 아닌
실행 도중 FrenchDeck2 객체를 생성할때 추상메서드의 구현 여부를 확인한다

MutableSequence
- 이때 , 추상메소드중 하나라도 구현되어 있지 않으면,
`FrenchDeck2를 생성할 수 없다는 메세지와 함꼐 ` + typeError를 발생시킴
"""


Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck2(collections.MutableSequence):
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

    def __setitem__(self, pos, value):  # 카드를 섞기 위해서 해당 메소드만 있어도된다
        self._cards[pos] = value

    def __delitem__(self, pos):  # MutableSeq 클래스를 상속했으므로, 구현해야한다
        del self._cards[pos]

    def insert(self, pos, value) -> None:  # MutableSeq 클래스를 상속했으므로, 구현해야한다
        self._cards.insert(pos, value)
