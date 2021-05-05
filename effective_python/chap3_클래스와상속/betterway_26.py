"""
26. 믹스인을 작성하는 방안을 고려하자.
- 다중 상속으로 얻는 편리함과 캡슐화가 필요하다면, 믹스인을 작성하는 방안을 고려하자.

mixin :
    - 클래스에서 제공해야 하는 추가적인 메소드만 정의하는 작은 클래스를 의미
    - 자체의 인스턴스 속성을 정의하지 않으며, __init__() 생성자를 호출하도록 요구하지 않는다.
"""


class ToDictMixIn(object):
    def to_dict(self):
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, instance_dict):
        for key, value in instance_dict.items():
            print(key, value)
