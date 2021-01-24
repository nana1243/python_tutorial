
import random

class BingCage:
    def __init__(self,items):
        self._items = list(items)
        random.shuffle(self._items)


    def pick(self):
        try:
            return  self._items.pop()
        except:
            raise  LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()


bingo = BingCage(items=[1,2,3])

for _ in range(3):
    print(bingo.pick())

boolean = callable(bingo)
print(boolean)
