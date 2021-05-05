"""
12.1 내장 자료형의 상속은 까다롭다
    -python 2.2전까지는 상속
"""


class DoppelDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


dd = DoppelDict(one=1)
print(dd)
