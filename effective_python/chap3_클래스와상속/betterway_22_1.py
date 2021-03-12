import collections

"""
**namedtuple의 제약**[무슨말인지 잘 모르겠음]
1. namedtuple로 만든 클래스에 기본 인수값을 설정 할 수 없다.그래서 데이터에 선택적인
 속성이 믾으면 다루기 힘들어진다, 속성을 사용할떄는 클래스를 직접 정의하는것이 나을 수 있다
2. namedtuple 인스턴스의 속성값을 여전히 숫자로 된 인덱스와 순회 방법으로 접근 할 수 있다.

클래스 리팩토링
1. 튜플을 점점 길게 확장하는 패턴은 딗셔너리의 계층을 깊게 두는 방식과 비슷하다.
2. 튜플의 아이템이 두개를 넘어가면, 다른 방법을 고려해야한다
3. collections 모듈의 nametuple 타입이 정확히 이런 요구에 부합한다.
3.1 nametuple은 작은 불변 데이터 클래스를 쉽게 정의할 수 있다.
"""

Grade = collections.namedtuple("Grade", ("score", "weight"))


class Subject(object):
    def __init__(self):
        self._grades = []

    def report_grades(self, score, weight):
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight

        return total / total_weight


class Student(object):
    def __init__(self):
        self._subject = {}

    def subject(self, name):
        if name not in self._subject:
            self._subject[name] = Subject()
        return self._subject[name]

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subject.values():
            total += subject.average_grade()
            count += 1
        return total / count


class Gradebook(object):
    def __init__(self):
        self._students = {}

    def student(self, name):
        if name not in self._students:
            self._students[name] = Student()
        return self._students[name]
