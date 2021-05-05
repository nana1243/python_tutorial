"""
hash 가능한 Vector2d
    - 해시가능하기 위해서는 불변형으로 만들어야한다
"""

from python_book.chap9.Vector2d import Vector2d

v1 = Vector2d(2, 4)
print(v1)
hash(v1)
