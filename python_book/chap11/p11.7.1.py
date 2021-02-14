import abc

"""
ABC를 선언할때는 abc.ABC or ABC를 상속하는 방법이 가장 좋다
"""


class MyABC(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def an_abstract_classmethod(
        cls,
    ):
        pass
