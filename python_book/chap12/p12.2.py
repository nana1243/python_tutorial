"""
1. 다이아몬드 문제
- 다중 상속을 지원하는 언어에서는 별개의 상위클래스가 동일한 이름으로
    메소드를 구현할떄 발생하는 이름 충돌 문제를 해결해출야한다
-- 파이썬에서도, 클래스명을 직접 명시한다

2. 객체 메서드를 클래스에 직접 호출할때는 self 를 반드시 명시해야 한다.
 - 바인딩 되지 않은 메서드에 접근하는 것이기 때문이

"""


class A:
    def ping(self):
        print("ping : ", self)


class B:
    def pong(self):
        print("pong: ", self)


class C(A):
    def pong(self):
        print("PONG ", self)


class D(B, C):
    def ping(self):
        A.ping(self)  # super().ping() 대신 호
        print("post-ping :", self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().ping()
        C.pong(self)


d = D()
d.pong()
print(D.__mro__)
C.pong(d)
