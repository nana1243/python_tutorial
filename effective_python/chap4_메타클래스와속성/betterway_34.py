"""
34. 메타클래스로 클래스의 존재를 등록하자
    - 메타 클래스를 사용하는 또 다른 일반적인 사례는 프로그램에 있는 타입을 자동으로 등록하는 것
    등록)
        - 간단한 식별자를 대응하는 클래스에 매핑하는 역방향 조회를 수행할때 유용

    -정리
        - 클래스 등록은 모듈 방식의 파이썬 프로그램을 만들때 유용한 패턴
        - 메타클래스를 이용하면, 프로그램에서 기반 클래스로 서브클래스를 만들때마다 자동으로 등록 코드를 실행가능
        - 메타클래스를 이용해, 클래스를 등록하면 등록 호출을 절대 빠뜨리지 않으므로 오류를 방직 가
"""
import json


class Serializable(object):
    def __init__(self, *args):
        self.args = args

    def serialize(self):
        return json.dumps({"args": self.args})


class Point2D(Serializable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point 2D (%d , %d)" % (self.x, self.y)


class Deserializable(object):
    @classmethod
    def deserializer(cls, json_data):
        params = json.loads(json_data)
        return cls(*params["args"])


point = Point2D(5, 3)
print("object : ", point)
print("Serialized  : ", point.serialize())

# 여기서의 문제는 직렬화된 데이터에 대응하는 타입을 미리 알고 있을때만
# 동작한다는 것!
# JSON으로 직렬화된 클래스를 많이 갖추고 , 그 중 어떤 클래스든
# 파이썬 객체로 역직렬화 하는 공통 함수를 만들자


class BetterSerializable(object):
    def __init__(self, *args):
        self.args = args

    def serialize(self):
        res = json.dumps({"class": self.__class__.__name__, "args": self.args})
        return res


# 다음은 클래스 이름을 해당 클래스의 객체 생성자에
# 매핑하고, 관리한다

registry = {}


def register_class(target_class):
    registry[target_class.__name__] = target_class


def deserialize(data):
    params = json.loads(data)
    name = params["class"]
    target_class = registry[name]
    return target_class(*params["args"])


# 그러나 registry에 등록한다는것을 까먹으면?
# error의 원인
# 메타클래스를 이 용하면 서브클래스가 정의될 때(Better way 33 “메타클래스로 서브클래스를 검증하자” 참고)
# class 문을 가로채는 방법으로 이렇게 만들 수 있다.


class Meta(type):
    def __new__(meta, name, bases, class_dict):
        cls = type.__new__(meta, name, bases, class_dict)
        register_class(cls)
        return cls


class RegisteredSerializable(BetterSerializable, metaclass=Meta):
    pass


# RegisteredSerializable의 서브클래스를 정의할 때 register_class가
# 호출되어 deserialize가 항상 기대한 대로 동작할 것이라고 확신할 수 있 다.
