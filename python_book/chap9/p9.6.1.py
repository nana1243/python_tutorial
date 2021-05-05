class Vector2d:
    typecode = "d"

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property  # getter의 의미를 둔다
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in range(int(self.x), int(self.y)))

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)
