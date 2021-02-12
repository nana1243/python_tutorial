import collections

"""
파이썬은 시퀀스를 찾아낸다
- 파이썬 데이터 모델은 가능 한 많은 핵심 프로토콜과 협업하겠다는 철학을 가짐
정리
- 시퀀스 프로토콜의 중요성 때문에 __iter__() 와 __contain__() 구현되지 않더라도,
    파이썬은 __getitem__()으로 대체 가능하다
- abc.Sequence를 상속하지 않지만, 시퀀스 프로토콜의 __getitem__(), __len__()
    을 구현한다
"""


class Foo:
    # __getitem__() 으로 부분 구현한 시퀀스 프로토콜
    # 항목에 접근할 수 있고, 반복할 수 있고, in을 사용할 수 있
    def __getitem__(self, pos):
        return range(0, 30, 10)[pos]


f = Foo()
print(f[1])

for i in f:
    print(i)

print(10 in f)
print(15 in f)


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
