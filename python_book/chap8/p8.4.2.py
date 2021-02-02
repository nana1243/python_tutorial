"""
가변 매개변수에 대한 방어적 프로그래밍
    - 중요한 것은 : 함수 구현자와 함수 호출자가 예상하는 것을 일치시키는 것이다
"""


baseketball_team = ["sue", "tina", "maya", "diana", "pat"]


class TwilightBus:
    """승객이 사라지게 만드는 버스 모델"""

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)
