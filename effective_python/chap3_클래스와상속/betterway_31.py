"""
31. 재사용 가능한 @property 메서드에는 디스크립터를 사용하자.
- @property로 데코레이터하는 메서드를 같은 클래스에 속한 여러 속성에 사용하지 못한다.

"""


class HomeWork(object):
    def __init__(self):
        self._grade = 0

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        if not (0 <= value <= 100):
            raise ValueError("Grade must be between 0 and 100")

        self._grade = value


class Exam(object):
    def __init__(self):
        self._writing_grade = 0
        self._math_grade = 0

    @staticmethod
    def _check_grade(value):
        if not (0 <= value <= 100):
            raise ValueError("Grade must be between 0 and 100")

    @property
    def writing_grade(self):
        return self._writing_grade

    @writing_grade.setter
    def writing_grade(self, value):
        self._check_grade(value=value)
        self._writing_grade = value

    @property
    def math_grade(self):
        return self._math_grade

    @math_grade.setter
    def math_grade(self, value):
        self._check_grade(value=value)
        self._math_grade = value


class Grade(object):
    def __init__(self):
        self._value = 0

    def __get__(self, instance, instance_type):
        return self._value

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError("grade must be between 0 and 100")
        self._value = value
