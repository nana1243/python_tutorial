from urllib.parse import parse_qs

"""
헬퍼 함수를 작성하자
"""

my_values = parse_qs("red=5&blue=7&green=", keep_blank_values=True)
print(repr(my_values))
