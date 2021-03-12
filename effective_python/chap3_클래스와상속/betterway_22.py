"""
better way22. 딕셔너리와 튜플보다는 헬퍼 클래스로 관리하자
- 딕셔너리 타입은 객체의 수명이 지속되는 동안 , 동적인 내부 상태를 관리하는 용도로 아주 좋다.
- **딕셔너리안에 딕셔너리를 담는 구조를 피해야 한다**
- 관리하기 복잡하다고 느끼는 즉시, 클래스로 옮겨가야 한다.

"""


class SimpleGradeBook(object):
    def __init__(self):
        self._grades = {}

    def add_students(self, name):
        self._grades[name] = []

    def report_students(self, name, score):
        self._grades[name].append(score)

    def average_students(self, name):
        grades = self._grades[name]
        return sum(grades) / len(grades)


class WeightGradeBook(object):
    def __init__(self):
        self._grades = {}

    def add_students(self, name):
        self._grades[name] = {}

    def report_grade(self, name, subject, score, weight):
        by_subject = self._grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append((score, weight))
