import os

"""
bytes3 , str, unicode의 차이점을 알자

* 파이썬3 애서는 bytes, str 두가지 타입으로 문자 시퀀스를 나타낸다
** bytes는 8비트 값을 저장한다
** str은 unicode문자를 저장한다

* 유니코드 문자를 바이너리 데이터(8비트) 표현하는 방법은 많다 ex)UTF-8
** 중요한건 , 파이썬 3의 str인스턴스와 파이썬2의 unicode 인스턴스와 연관된 바이너리 인코딩이 없다는 점이다
** 유니코드 문자를 바이너리 데이터로 변환하려면, encode 메서드를 사용해야한다
** 바이너리 코드를 유니코드 문자로 변환하려면, decode 메소드를 사용해야한다

* 문자 타입에 분리되어 있는 탓에, 파이썬은 2가지 상황에 부딪힌다
** UTF-8으로 인코드된 문자인 8비트로 처리하려는 상항
** 인코딩이 없는 유니코드 문자를 처리하려는 상황

*파이썬 3에서 내장 함수 open이 반환하는 파일 핸들을 사용하는 연산은 기본으로 UTF-8 인코딩을 사용한다는 점이다.
** 문제가 일어난 이유는 파이썬3의 open에 새 encoding 인수가 추가되었기 떄문이

"""


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode("utf-8")
    else:
        value = bytes_or_str
    return value  # str 인스턴


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode("utf-8")
    else:
        value = bytes_or_str
    return value  # bytes 인스턴스


with open("tmp.bin", "w") as f:
    f.write(os.urandom(10))
# TypeError: write() argument must be str, not bytes
# 'wb'를 통해 바이너리 쓰기 모드로 사용해야한

with open("tmp.bin", "wb") as f:
    f.write(os.urandom(10))


"""
정리
1. 파이썬3 에서는 bytes는 8비트로 저장하고, str은 유니코드 문자를 저장한다
2. 헬퍼함수를 사용해서 , 처리할 입력값이 원하는 문자 시퀀스 타입(8비트값, UTF-8, 유니코드 문자)으로 되어 있게 한다
3. 바이너리 데이터를 파일에서 읽거나 쓸떄는 파일을 바이너리 모드로 오픈한다
"""
