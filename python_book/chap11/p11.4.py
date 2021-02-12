from collections import abc

"""
알렉스 마르텔리의 물새
- ABC가 파이썬에 큰 도움이 되는 이유에 대해 알렉스 마르텔리를 통해 듣자
#noqa:W291
1. 덕타이핑
- 객체의 실제 자료형은 무시하고, 대신 객체 용도에 맞는 메소드 이름, 시그니처,
    의미를 구현하도록 보장하는데 주안점을 둔다
    = 파이썬에서는 결국 자료형 검사를 위한 isinstancd() 함수 사용회피

- 전반적으로 덕 타이핑 방법이 상당히 유용하게 사용되는 상황이 많지만,
그렇지 않은 상황에서도 다른 방법으로 발전됨

2. 우연한 유사성은 프로그래밍에서도 발생

- 구스타이핑 : cls가 추상 베이스 클래스인 경우, #noqa:W291
    - 즉 cls 메타클래스가 abc.ABCMeta인 경우
    -  isinstancd(obj,cls)를 써도 좋다는 의미
"""


class Artist:
    def draw(self):
        """그림그리기"""


class Gunslinger:
    def draw(self):
        """총을 뽑는 행위"""


class Lottery:
    def draw(self):
        """복권 추첨"""


class Struggle:
    def __len__(self):
        return 23


# abc.Sized 클래스는 Struggle의 `일종의 서브 클래스` 인식
print(isinstance(Struggle(), abc.Sized))

"""
정리
1. numbers, collections.abc 혹은 여러분이 사용할 다른 프레임워크에 #noqa:W291
    있는 ABC가 표현하는 개념을 실현하는 클래스로 구현할때는 언제나 해당 #noqa:W291
    ABC를 상속하거나 해당 ABC에 등록하라 #noqa:W291
2. 절대로 ABC나 메타다클래스를 직접 구현하지 `말라`
3. `구스 타이핑` 이라는 말을 만들어낸 것 외에도 알렉스는 필요한 메서드를
    구현하는것보다 ABC를 상속하는 것이 낫다고 강조한다
    - 상속은 개발자의 의도를 명확하게 드러낼 수 있다
** ABC를 우리가 직접 생성하지 말아야 한다**
- ABC는 `시퀀스`나, `정확한 숫자` 같은 일종의 프레임워크가 소개하는
    개념이나, 추상성을 담기 위한 것이다
- 기존 ABC를 제대로 사용하는 것만으로도 잘못된 설계 위험 없이 99.9%
    혜택을 볼 것 다
"""

field_names = "hennie,jennie,queen"
try:
    field_names = field_names.replace(",", "").split()
except AttributeError:
    pass

field_names = tuple(field_names)
print(field_names)
